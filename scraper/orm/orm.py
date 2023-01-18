import os

from sqlalchemy import Date
from sqlalchemy import Column
from sqlalchemy import DECIMAL
from sqlalchemy import Integer
from sqlalchemy import VARCHAR
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Trades(Base):
    __tablename__ = 'trades'
    
    id = Column(Integer, primary_key=True)
    filingDate = Column(DateTime)
    tradeDate = Column(Date)
    ticker = Column(VARCHAR(8))
    companyName = Column(VARCHAR(256))
    insiderName = Column(VARCHAR(128))
    insiderTitle = Column(VARCHAR(64))
    tradeType = Column(VARCHAR(64))
    price = Column(DECIMAL(13, 2))
    qty = Column(Integer)
    owned = Column(Integer)
    deltaOwned = Column(Integer)
    value = Column(Integer)
    
    def __init__(self, filing_date, trade_date, ticker, company_name, insider_name, insider_title, trade_type, price, qty, owned, delta_owned, value):
        self.filingDate = filing_date
        self.tradeDate = trade_date
        self.ticker = ticker
        self.companyName = company_name
        self.insiderName = insider_name
        self.insiderTitle = insider_title
        self.tradeType = trade_type
        self.price = price
        self.qty = qty
        self.owned = owned
        self.deltaOwned = delta_owned
        self.value = value
    
    def __repr__(self):
        return f"<{self.ticker} {self.tradeDate}>"
