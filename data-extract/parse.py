from bs4 import BeautifulSoup
from requests import get as GET

URL = "http://openinsider.com/screener"
QUERY_PARAMS = {
    'sortcol': 1,
    'cnt': 1000,
    'td': 0,
    'fd': 730,
    'xp': 1,
    'xs': 1,
    'sic1': -1,
    'sicl': 100,
    'sich': 9999,
    'grp': 0,
    'page': 1
}
tURL = "http://openinsider.com/screener?fd=730&td=0&xp=1&xs=1&sic1=-1&sicl=100&sich=9999&grp=0&sortcol=1&cnt=100&page=1"
# res = GET(URL, params=QUERY_PARAMS)
res = GET(tURL)
print(res.text)
html = BeautifulSoup(res.text, 'html.parser')
table = html.find_all('table', 'tinytable')
# print(table)