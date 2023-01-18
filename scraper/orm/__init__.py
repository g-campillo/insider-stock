import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .orm import Trades

load_dotenv()
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DATABASE")
engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()