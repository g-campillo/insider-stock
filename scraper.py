import os
import sys
import json
import logging as log
from time import sleep
from argparse import ArgumentParser

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests import get as GET
from jinja2 import Environment
from jinja2 import FileSystemLoader

from emailer import Email

class Scraper:
    
    # The default parameters gets the last 100 purchases sorted by the trade date
    def __init__(self, 
                fd=730, 
                td=0, 
                xp=1, 
                sic1=-1, 
                sicl=100, 
                sich=9999, 
                grp=0, 
                sortcol=1, 
                cnt=100, 
                page=1,
                sleep_interval=300):
        
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
        self.SLEEP_INTERVAL = sleep_interval
        self.URL = os.environ.get("STOCK_URL")
        
        self.email = Email(
            host=os.environ.get("EMAIL_HOST"),
            port=int(os.environ.get("EMAIL_PORT")),
            username=os.environ.get("EMAIL_USER"),
            password=os.environ.get("EMAIL_PASSWORD")
        )
        
        self.current_data = set()
    
    # Just in case the request fails
    def _make_request(self):
        try:
            log.info("Requesting HTML page")
            return GET(self.URL, params=self.QUERY_PARAMS)
        except Exception as e:
            log.error("Error making GET request for HTML page")
            log.debug(msg=e, exc_info=True)
    
    def _clean_string(self, text):
        return text \
                .replace("$", "") \
                .replace(",", "") \
                .replace("+", "") \
                .replace("%", "")
    
    def get_data(self):
        
        try:
            log.info("Getting data")
            self.HTML = BeautifulSoup(self._make_request().text, "html.parser")
            data_rows = self.HTML.findAll("tbody")[1].findChildren("tr")
            
            agg_data = []
            
            for row in data_rows:
                table_data = row.findChildren("td")
                
                filing_date = table_data[1].findChildren("a")[0].string
                trade_date = table_data[2].findChildren("div")[0].string
                ticker = table_data[3].findChildren("a")[0].string
                company_name = table_data[4].findChildren("a")[0].string
                insider_name = table_data[5].findChildren("a")[0].string
                insider_title = table_data[6].string
                trade_type = table_data[7].string
                price = table_data[8].string
                qty = table_data[9].string
                owned = table_data[10].string
                delta_owned = table_data[11].string
                value = table_data[12].string
                
                data = {
                    "filing_date": filing_date,
                    "trade_date": trade_date,
                    "ticker": ticker,
                    "company_name": company_name,
                    "insider_name": insider_name,
                    "insider_title": insider_title,
                    "trade_type": trade_type,
                    "price": price,
                    "qty": qty,
                    "owned": owned,
                    "delta_owned": delta_owned,
                    "value": value
                }
                
                # data = [
                #     f"<br>"
                #     f"Ticker: {ticker}<br>",
                #     f"Company name: {companyName}<br>",
                #     f"Filing date: {filingDate}<br>",
                #     f"Trade date: {tradeDate}<br>",
                #     f"Price: {price}<br>",
                #     f"Quantity: {qty}<br>",
                #     f"Value: {value}<br>",
                #     f"Owned: {owned}<br>",
                #     f"Delta owned: {deltaOwned}<br>",
                #     f"Trade type: {tradeType}<br>",
                #     f"Insider Name: {insiderName}<br>",
                #     f"Insider title: {insiderTitle}<br>",
                #     "-" * 25
                # ]
                agg_data.append(data)
            log.debug(f"Data gathered: {agg_data}")
            return agg_data
        except Exception as e:
            log.error("There was an error collecting the data from the site")
            log.debug(msg=e, exc_info=True)
    
    def _remove_duplicates(self, data):
        data = set(data)
        new_data = data - self.current_data
        self.current_data = data
        return new_data
    
    def _format_data(self, data):
        env = Environment(loader=FileSystemLoader("templates/"))
        template = env.get_template("email_template.j2")
        res = template.render(data)
        log.debug(res)
    
    # stores data directly to the database
    def _send_email(self, data):    
        try:
            self._format_data(data)
            return
            self.email.send(
                subject=os.environ.get("EMAIL_SUBJECT"),
                body=data,
                recipients=os.environ.get("EMAIL_RECIPIENTS").split(",")
            )
            log.info("Email was sent!")
        except Exception as e:
            log.error("An error occurred during data upload")
            log.debug(msg=e, exc_info=True)
    
    def run(self):
        try:
            while True:
                self._send_email(self.get_data())
                sleep(self.SLEEP_INTERVAL)
        except KeyboardInterrupt:
            log.warning("Program was manually stopped")
            sys.exit(0)
        except Exception as e:
            log.error("An error occurred in the main loop")
            log.debug(msg=e, exc_info=True)

if __name__ == "__main__":
    load_dotenv()
    
    log.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(funcName)s] %(message)s",
        level=log.DEBUG
    )
    
    parser = ArgumentParser()
    parser.add_argument("--sleep-interval", type=int, required=False, help="The amount of seconds to sleep after each run")
    
    args = parser.parse_args()
    
    Scraper(
        sleep_interval=args.sleep_interval or 300
    ).run()
