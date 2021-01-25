from data import db
import requests
import countDown
from data import repository

if __name__ == '__main__':
    session = requests.session()
    headers, url = countDown.count_down
    r = session.get(url, headers=headers, allow_redirects=True)
    data = r.json()
    repository.dispose_json(data['products']['items'])

