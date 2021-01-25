import logging

from data import db

logging.basicConfig(level=logging.DEBUG)
db.create_engine(dsn='LNMServer', uid='sa', pwd='P@ssw0rd')