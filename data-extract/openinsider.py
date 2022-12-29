from bs4 import BeautifulSoup
from requests import get as GET

class OpenInsiderParser:
    
    def __init__(self, set_purchases=1, sortcol=1, cnt=100):
        self.URL = 'http://openinsider.com/screener'
        self.QUERY_PARAMS = {
            'xp': set_purchases, # set purchases checkbox
            'sortcol': sortcol, # the column to sort by
            'cnt': cnt # the amount of records to return
        }
        
        self._html = None
    
    def get_records(self):
        res = GET(self.URL, params=self.QUERY_PARAMS)
        self._html = BeautifulSoup(res.text, 'html.parser')
        records = self._find_records(self._html)
        return self._clean_data(records)

    def _find_records(self, html):
        data = html.find('div', {'id': 'results'}) \
                .next_sibling \
                .next_sibling \
                .tbody \
                .findChildren()
        
        return data
    
    def _clean_data(self, records):
        res = []
        for child in records:
            properties = child.findAll(text=True)
            if len(properties) == 13:
                filtered_data = {
                    'filingDate': properties[0],
                    'tradeDate': properties[1],
                    'ticker': properties[3],
                    'company': properties[4],
                    'insiderName': properties[5],
                    'insiderPosition': properties[6],
                    'transactionType': properties[7],
                    'purchasePrice': properties[8],
                    'qty': properties[9],
                    'owned': properties[10],
                    'deltaOwnPercentage': properties[11],
                    'value': properties[12]
                }
                res.append(filtered_data)
        return res
