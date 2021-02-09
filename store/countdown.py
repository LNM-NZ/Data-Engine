from store.common import _common_headers
from store.common import Store

_headers = {
           'accept': 'application/json, text/plain, */*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
           'cache-control': 'no-cache',
           'content-type': 'application/json',
           'cookie': '_ga=GA1.3.304982317.1610101053; _gcl_au=1.1.330398016.1610101054;'
                     ' _vwo_uuid_v2=DF61EA991A5411C9583DFC48D05643F4F|1ea29062fdf928835a9506bef5d2293a;'
                     ' _hjid=d4025d82-2cce-4d30-9b4d-29d1b0faa9e2; _fbp=fb.2.1610101054724.161958792;'
                     ' gig_bootstrap_3_-SfMo7rbUCn0p7mhjsDfYu8T5axQEv6QEEK9Edz5fo-fZombWKJzRgCf1-js9O2g=login_ver3;'
                     ' cd_user_id=176e18062475ba-0318571ae32fc3-163b6152-fa000-176e1806248bb7;'
                     ' ai_user=wIZ3G|2021-01-08T10:18:10.485Z;'
                     ' gig_bootstrap_3_PWTq_MK-V930M4hDLpcL_qqUx224X_zPBEZ8yJeX45RHI-uKWYQC5QadqeRIfQKB=login_ver3;'
                     ' kampyle_userid=0974-4d8e-88fe-421f-0ec6-0dc4-6c49-72f1; _gid=GA1.3.1729880539.1611395016;'
                     ' _hjTLDTest=1; ARRAffinity=ba6dced8d7601eacc783680b2a1cf55048b686b99e16a0b39da07afa8305314d;'
                     ' ARRAffinitySameSite=ba6dced8d7601eacc783680b2a1cf55048b686b99e16a0b39da07afa8305314d;'
                     ' dtid=2:SvrWMYSOsiQ2qevFvTKKzBfMvS1EfV3UTP90ccxIV7m8uL6x4TXCnTsU4rKYd2RninyJDav+'
                     '9jLBB0bXQSRvE7Hd+y/UasKvDFqy8VGQkXV6AtKEgfvPohrCPwauT8j+fKA=;'
                     ' ASP.NET_SessionId=0go0oyeebcafmlr2w3hrije4; cw-laie=50b80490074e4b40a3f38ca5fc25d2bb;'
                     ' __RequestVerificationToken=pNB__dESlBW0VsYQNQQD_DdByuXAv-rlrzTUYpmqyBGPN8i8M5utgtj71'
                     'tPkwViobPtiKZZ90KaZMOn_qEkAOoyDiT5Fd1aVguPNOMwhMuM1;'
                     ' gig_canary=false; gig_canary_ver=11633-1-26857410; _hjIncludedInSessionSample=0;'
                     ' cw-arjshtsw=n0e54343048644067bf1c5127ef6ca357nuvkzduin; kampyleUserSession=1611447077469;'
                     ' kampyleUserSessionsCount=6; kampyleSessionPageCounter=1; AKA_A2=A;'
                     ' akavpau_vpshop=1611451491~id=372324913c0fc704ca323c4b380c15ce;'
                     ' ai_sessioncw-=+hmi5|1611451191461.79|1611451191461.79;'
                     ' _dc_gtm_UA-10765339-1=1',
           'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
           'pragma': 'no-cache',
           'referer': 'https://shop.countdown.co.nz/shop/specials?promo_position=Tile'
                      '&promo_creative=CTA%20button&promo_name=%20-%20Specials%20Hub&itemID=All%20Specials',
           'request-id': '|c16aaf76e9ed4b89ad56f981d6368752.1e100014f8934ec6',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'x-requested-with': 'OnlineShopping.WebApp'}
_url = 'https://shop.countdown.co.nz/api/v1/products?target=specials' \
      '&promo_position=Tile&promo_creative=CTA%20button&promo_name=%20-%20Specials%20Hub&itemID=All%20Specials'
_headers.update(_common_headers)
count_down = Store(headers=_headers, url=_url, query=None)
