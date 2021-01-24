import pyodbc

conn = pyodbc.connect('DSN=LNMServer;UID=sa;PWD=P@ssw0rd')


def update_json(json):
    for item in json:
        print('name={0}, brand={1}'.format(item['name'], item['brand']))
