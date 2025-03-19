import requests

from config_date.config import URL


def get():
    url = URL
    product = []
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://www.wildberries.ru',
            'priority': 'u=1, i',
            'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'x-captcha-id': 'Catalog 1|1|1743102137|AA==|964e40bfe3494fd498c8fae52fea85d5|cZh1V1dMh2mIV5O3AHdCUF60FDderiFmiLImQObHR7M',
            'x-queryid': 'qid1019963140173680077520250313190224',
        }

        params = {
            'ab_testing': 'false',
            'appType': '1',
            'curr': 'rub',
            'dest': '-2133466',
            'lang': 'ru',
            'page': '1',
            'query': 'наушники',
            'resultset': 'catalog',
            'sort': 'popular',
            'spp': '30',
            'suppressSpellcheck': 'false',
        }

        result = requests.get(url, params=params, headers=headers).json()
        products_row = result.get('data', {}).get('products', None)
        if products_row is not None and len(products_row) > 0:
            for elem in products_row:
                product.append({
                    'brand': elem.get('brand', None),
                    'colors': elem.get('colors', None),
                    'priceU': float(elem.get('sizes', None)[0].get('price', {}).get('basic',
                                                                                    None)) / 100 if elem is not None else None,
                    'salePriceU': float(
                        elem.get('sizes', None)[0].get('price', {}).get('product')) / 100 if elem is not None else None,
                    'supplier': elem.get('supplier'),
                    'rating': elem.get('reviewRating'),
                    'feedbacks': elem.get('feedbacks'),
                    'id': elem.get('id')
                })
        return product
    except:
        print('Неверный запрос-ссылка')


result_get = get()
sorted_low = sorted(result_get, key=lambda x: x['salePriceU'])
sorted_high = sorted(result_get, key=lambda x: x['salePriceU'], reverse=True)
sorted_rating = sorted(result_get, key=lambda x: x['rating'], reverse=True)
