from Data_Science.models import User, BedHours, Mood, Tiredness, db

#get username from front end
username = "testuser"

user_id = db.session.query(User.id).filter(User.username == username).one()
hours_in_bed = db.session.query(BedHours.waketime).filter(BedHours.user_id == user_id).all()
