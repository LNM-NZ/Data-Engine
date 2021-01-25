import functools
import threading
import logging


class _Engine(object):
    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect

# cnxn = pyodbc.connect('DSN=LNMServer;UID=sa;PWD=P@ssw0rd')


engine = None


class _Connection(object):
    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            cnxt = engine.connect()
            logging.info('open connection {0}...'.format(hex(id(cnxt))))
            self.connection = cnxt
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def cleanup(self):
        if self.connection:
            conn = self.connection
            self.connection = None
            logging.info('close connection <{0}>...'.format(hex(id(conn))))
            conn.close()


def create_engine(dsn, uid, pwd):
    global engine
    if engine is not None:
        raise Exception('Engine has already been initialized.')
    import pyodbc
    engine = _Engine(pyodbc.connect(DSN=dsn, UID=uid, PWd=pwd))
    # test connection
    logging.info('SqlServer is initialized as {0}'.format(hex(id(engine))))


class _DbContext(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return self.connection is not None

    def init(self):
        self.connection = _Connection()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()


_db_ctx = _DbContext()


class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()


def connection():
    return _ConnectionCtx()


class _TransactionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions == 0:
                if exc_type is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()

    def commit(self):
        global _db_ctx
        try:
            _db_ctx.connection.commit()
        except Exception:
            _db_ctx.connection.rollback()
            raise

    def rollback(self):
        global _db_ctx
        _db_ctx.connection.rollback


def connection_unit(func):
    """
    Decorator for connection
    """
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with _ConnectionCtx():
            return func(*args, **kw)
    return _wrapper


@connection_unit
def _execute(sql, *args):
    global _db_ctx
    cursor = None
    # sql = sql.replace('?', '%s')
    logging.info('SQL: {0}, ARGS: {1}'.format(sql, args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql, args)
        r = cursor.rowcount
        if _db_ctx.transactions == 0:
            # no transaction environment:
            logging.info('auto commit')
            _db_ctx.connection.commit()
        return r
    finally:
        if cursor:
            cursor.close()


def insert(table, **kw):
    """

    :param table:
    :param kw:
    :return:
    """
    cols, args = zip(*kw.items())
    sql = 'insert into {0} ({1}) values ({2})'.\
        format(table, ','.join(['{0}'.format(col) for col in cols]), ','.join(['?' for i in range(len(cols))]))
    return _execute(sql, *args)


def update_json(json):
    for item in json:
        print('name={0}, brand={1}'.format(item['name'], item['brand']))
