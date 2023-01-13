import sys

from bs4 import BeautifulSoup
from requests import get as GET

class Scraper:
    
    # The default parameters gets the last 100 purchases sorted by the trade date
    def __init__(self, fd=730, td=0, xp=1, sic1=-1, sicl=100, sich=9999, grp=0, sortcol=1, cnt=100, page=1):
        self.URL = "http://openinsider.com/screener"
        self.QUERY_PARAMS = {
            "fd": fd,
            "td": td,
            "xp": xp,
            "sic1": sic1,
            "sicl": sicl,
            "sich": sich,
            "grp": grp,
            "sortcol": sortcol,
            "cnt": cnt,
            "page": page
        }
        
        self.HTML = None
    
    # Just in case the request fails
    def _make_request(self):
        try:
            return GET(self.URL, params=self.QUERY_PARAMS)
        except:
            print('There was an error making the request')
    
    def parse_data(self):
        
        try:
            self.HTML = BeautifulSoup(self._make_request().text, "html.parser")
            data_rows = self.HTML.findAll("tbody")[1].findChildren("tr")
            
            agg_data = []
            
            for row in data_rows:
                table_data = row.findChildren("td")
                
                data = {
                    "filing_date": table_data[1].findChildren("a")[0].string,
                    "trade_date": table_data[2].findChildren("div")[0].string,
                    "ticker": table_data[3].findChildren("a")[0].string,
                    "company_name": table_data[4].findChildren("a")[0].string,
                    "insider_name": table_data[5].findChildren("a")[0].string,
                    "insider_title": table_data[6].string,
                    "trade_type": table_data[7].string,
                    "price": table_data[8].string,
                    "qty": table_data[9].string,
                    "owned": table_data[10].string,
                    "delta_own": table_data[11].string,
                    "value": table_data[12].string
                }
                agg_data.append(data)
            return agg_data
        except:
            print("There was an error aggregating the data")



if __name__ == '__main__':
    scraper = Scraper()
    data = scraper.parse_data()
    for item in data:
        print(item)