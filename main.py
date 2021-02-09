import requests
from store import target_stores
from data import repository
from store.common import Store

if __name__ == '__main__':
    session = requests.session()

    for item in target_stores:
        headers, url, query = item
        if query is not None:
            url = url + "?"
            for key, value in query.items():
                q = "{0}={1}&".format(key, value);
                url = url + q
        print(url)
        r = session.get(url, headers=headers, allow_redirects=True)
        content_type = r.headers['content-type']
        if 'application/json' in content_type:
            data = r.json()
            repository.dispose_json(data['products']['items'])
        elif 'text/html' in content_type:
            r.encoding = 'utf-8'
            repository.dispose_html(r.text)
