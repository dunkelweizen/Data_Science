from Data_Science.create_database import User, BedHours, Mood, Tiredness, db
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

#get username from front end
username = "testuser"

df = pd.DataFrame()

user_id = db.session.query(User.id).filter(User.username == username).one()
bedtimes = db.session.query(BedHours.bedtime).filter(BedHours.user_id == user_id).all()
bedtimes_ids = db.session.query(BedHours.night_id).filter(BedHours.user_id == user_id).all()
waketimes = db.session.query(BedHours.waketime).filter(BedHours.user_id == user_id).all()
morning_mood_list = []
midday_mood_list = []
evening_mood_list = []
morning_tired_list = []
midday_tired_list = []
evening_tired_list = []
for id in bedtimes_ids:
    morning_mood = db.session.query(Mood.wake_mood).filter(Mood.night_id == id)
    morning_mood_list.append(morning_mood)
    midday_mood = db.session.query(Mood.midday_mood).filter(Mood.night_id == id)
    midday_mood_list.append(midday_mood)
    evening_mood = db.session.query(Mood.night_mood).filter(Mood.night_id == id)
    evening_mood_list.append(evening_mood)
    morning_tired = db.session.query(Tiredness.wake_tired).filter(Mood.night_id == id)
    morning_tired_list.append(morning_tired)
    midday_tired = db.session.query(Tiredness.midday_tired).filter(Tiredness.night_id == id)
    midday_tired_list.append(midday_tired)
    evening_tired = db.session.query(Tiredness.night_tired).filter(Tiredness.night_id == id)
    evening_tired_list.append(evening_tired)

for i in range(len(bedtimes)):
    df['bedtime'].iloc[i] = bedtimes[i]
    df['waketime'].iloc[i] = waketimes[i]
    df['night_id'].iloc[i] = bedtimes_ids[i]
    df['morning_mood'].iloc[i] = morning_mood_list[i]
    df['midday_mood'].iloc[i] = midday_mood_list[i]
    df['evening_mood'].iloc[i] = evening_mood_list[i]
    df['morning_tired'].iloc[i] = morning_tired_list[i]
    df['midday_tired'].iloc[i] = midday_tired_list[i]
    df['evening_tired'].iloc[i] = evening_tired_list[i]


