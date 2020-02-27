import os
import psycopg2
from dotenv import load_dotenv
from Data_Science.models import BedHours, Mood, Tiredness, db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
conn = psycopg2.connect(dbname=DATABASE_USER, user=DATABASE_USER, host=DATABASE_HOST, password=DATABASE_PASSWORD)
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
meta=MetaData()

meta.create_all(engine)





