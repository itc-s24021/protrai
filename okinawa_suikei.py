#24021
#沖縄県の推計人口のページより最新情報をスクレイピングするpythonコード
#https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri =  'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = 'Shift_JIS'

#print(html.text)
