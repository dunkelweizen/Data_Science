from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy
migrate = Migrate()


class User(db.Model):
    username = db.Column(db.String(128))
    id = db.Column(db.BIGINT, primary_key=True)


class BedHours(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT, db.ForeignKey("user.id"))
    bedtime = db.Column(db.DateTime)
    waketime = db.Column(db.DateTime)


class Mood(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    night_id = db.Column(db.BIGINT, db.ForeignKey("bedhours.id"), nullable=False)
    wake_mood = db.Column(db.Integer)
    midday_mood = db.Column(db.Integer)
    night_mood = db.Column(db.Integer)


class Tiredness(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    night_id = db.Column(db.BIGINT, db.ForeignKey("bedhours.id"), nullable=False)
    wake_tired = db.Column(db.Integer)
    midday_tired = db.Column(db.Integer)
    night_tired = db.Column(db.Integer)
