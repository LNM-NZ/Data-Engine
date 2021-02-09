from data import db
from bs4 import BeautifulSoup


def dispose_json(json):
    params = dict(Name='test')
    # db.insert('LNMBase.dbo.Brand', **params)


def dispose_html(text):
    bs = BeautifulSoup(text, 'html.parser')
    goods = bs.findAll('div', {'class': ['js-product-card-footer', 'fs-product-card__footer-container']})

    for item in goods:
        print(item['data-options'])
