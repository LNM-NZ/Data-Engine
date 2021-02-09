from store.common import _common_headers
from store.common import Store

_url = 'https://www.paknsaveonline.co.nz/category/fresh-foods-and-bakery/fruit--vegetables/fresh-vegetables'
_headers = {
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                         'q=0.8,application/signed-exchange;v=b3;q=0.9',
               # 'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
               'cache-control': 'max-age=0',
               'cookie': 'server_nearest_store={"StoreId":"65defcf2-bc15-490e-a84f-1f13b769cd22",'
                         '"UserLat":"-36.7443","UserLng":"174.6947","StoreLat":"-36.729975",'
                         '"StoreLng":"174.706725","IsSuccess":true}; _gaexp=GAX1.3.omhxY3A0Rvq3T5O9elQB1A.18676.1; '
                         '_rollupGA=GA1.3.1754054871.1610100722; _fbp=fb.2.1610100739894.1219482194; '
                         '_hjid=39d5b9d5-0f38-4608-9797-6adb7b9081c9; _ga=GA1.3.1754054871.1610100722; '
                         '_gcl_au=1.1.1710989745.1610100741; '
                         'SC_ANALYTICS_GLOBAL_COOKIE=4807d76d20f548458a7c0ebedee05988|True; '
                         'ASP.NET_SessionId=eq0s535k1afibam24w4c3ua2; '
                         '__RequestVerificationToken=307wGhdD6U0Rvq39cuk6WOPx8yy54jK-ZnI'
                         '2cwOwtrYQa37EPRahRPQHtQQkdeNniQhhnc5Wa1CPm07LuYJ71juYbrw1; '
                         'sxa_site=PAKnSAVE; _rollupGA_gid=GA1.3.1508564286.1612692066; '
                         '_gid=GA1.3.360321736.1612692283; _hjTLDTest=1; fs-store-select-tooltip-closed=true; '
                         '__cfduid=daa777938cc637edb2eb87045324861621612692875; '
                         '_gac_UA-136314956-1=1.1612692678.Cj0KCQiAvP6ABhCjARIsAH37rbSHS7zLYghL'
                         'JFSCuCwM9ByuOXHExQPhAmoQiH6QH8YHEYdAKE6dpaIaAr6WEALw_wcB; '
                         'ki_r=; _hjIncludedInSessionSample=0; SessionCookieIdV2=963ec79e4bbe48fa830013660ed0cd6c; '
                         'UserCookieV1=2200659478; STORE_ID=65defcf2-bc15-490e-a84f-1f13b769cd22|False; '
                         '_gat_UA-136314956-1=1; '
                         '_dc_gtm_UA-123048662-1=1; f_triggerGenericSurvey=1612731526351; '
                         'ki_t=1610100740861%3B1612692288997%3B1612731526812%3B4%3B67; _gat_UA-123048662-1=1',
               'referer': 'https://www.paknsaveonline.co.nz/deals',
               'sec-fetch-dest': 'document',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests': '1',

}
_query = {
    'pg': 1
}

_headers.update(_common_headers)
paknsave = Store(headers=_headers, url=_url, query=_query)
