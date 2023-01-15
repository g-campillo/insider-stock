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