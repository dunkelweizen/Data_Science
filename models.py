from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()


db = SQLAlchemy()


class User(Base):
    __tablename__ = 'user'
    username = db.Column(db.String(128))
    id = db.Column(db.BIGINT, primary_key=True)


class BedHours(Base):
    __tablename__ = 'bedhours'
    id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT, db.ForeignKey("user.id"))
    bedtime = db.Column(db.DateTime)
    waketime = db.Column(db.DateTime)


class Mood(Base):
    __tablename__ = 'mood'
    id = db.Column(db.BIGINT, primary_key=True)
    night_id = db.Column(db.BIGINT, db.ForeignKey("bedhours.id"), nullable=False)
    wake_mood = db.Column(db.Integer)
    midday_mood = db.Column(db.Integer)
    night_mood = db.Column(db.Integer)


class Tiredness(Base):
    __tablename__ = 'tiredness'
    id = db.Column(db.BIGINT, primary_key=True)
    night_id = db.Column(db.BIGINT, db.ForeignKey("bedhours.id"), nullable=False)
    wake_tired = db.Column(db.Integer)
    midday_tired = db.Column(db.Integer)
    night_tired = db.Column(db.Integer)
