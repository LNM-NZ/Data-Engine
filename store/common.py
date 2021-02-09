from collections import namedtuple

_common_headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36'
                                 ' (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
Store = namedtuple('Store', 'headers url query')
