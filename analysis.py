from Data_Science.create_database import User, BedHours, Mood, Tiredness
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import select
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
connection = engine.connect()

# get username from front end
username = "Manuela9"

df = pd.DataFrame()

user_id = connection.execute(select([User.id]).where(User.username == username))
for result in user_id:
    user_id = result[0]
print(user_id)
bedtimes = connection.execute(select([BedHours.bedtime]).where(BedHours.user_id == user_id))
bedtimes_ids = connection.execute(select([BedHours.id]).where(BedHours.user_id == user_id))
waketimes = connection.execute(select([BedHours.waketime]).where(BedHours.user_id == user_id))
morning_mood_list = []
midday_mood_list = []
evening_mood_list = []
morning_tired_list = []
midday_tired_list = []
evening_tired_list = []
for id in bedtimes_ids:
    morning_mood = connection.execute(select([Mood.wake_mood]).where(Mood.night_id == id[0]))
    for result in morning_mood:
        morning_mood_list.append(result[0])
    midday_mood = connection.execute(select([Mood.midday_mood]).where(Mood.night_id == id[0]))
    for result in midday_mood:
        midday_mood_list.append(result[0])
    evening_mood = connection.execute(select([Mood.night_mood]).where(Mood.night_id == id[0]))
    for result in evening_mood:
        evening_mood_list.append(result[0])
    morning_tired = connection.execute(select([Tiredness.wake_tired]).where(Mood.night_id == id[0]))
    for result in morning_tired:
        morning_tired_list.append(result[0])
    midday_tired = connection.execute(select([Tiredness.midday_tired]).where(Tiredness.night_id == id[0]))
    for result in midday_tired:
        midday_tired_list.append(result[0])
    evening_tired = connection.execute(select([Tiredness.night_tired]).where(Tiredness.night_id == id[0]))
    for result in evening_tired:
        evening_tired_list.append(result[0])

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

# need to create model to predict hours necessary for maximum mood/lowest tiredness
# target is hours in bed
# create prediction with input of mood/tiredness integers
# train model on each user, then create prediction of hours_in_bed with all 4s for mood and 1s for tired
X = df.drop('hours_in_bed', axis=1)
X = df.drop('bedtime', axis=1)
X = df.drop('waketime', axis=1)
y = df['hours_in_bed']

model = LinearRegression()

model.fit(X,y)
print(X.columns)