from data import db


def dispose_json(json):
    params = dict(Name='test')
    db.insert('LNMBase.dbo.Brand', **params)
