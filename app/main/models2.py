from turtle import title
from unicodedata import category

from app.main.views import index
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager

class Pitches(db.Model):

    __tablename__ = 'pitches_table'

    id = db.Column(db.Integer,primary_key = True)
    # pitch_id = db.Column(db.Integer)
    title = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    comment =db.relationship('Comments', backref='title', lazy='dynamic')
    
    # new_pitch= pitches_table(pitch_id="",pitch_title="interview",pitch_category="interview",the_pitch="hello iam ian",posted="",user_id="",comment="")


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches= Pitches.querry.filter_by(category=category).all()
        return pitches


    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(comment_id=id).all()
        return comments

    @classmethod
    def getPitchId(cls, id):
        pitch = Pitches.query.filter_by(id=id).first()
        return pitch
    @classmethod
    def clear_pitches(cls):
        Pitches.all_pitches.clear()
    def __repr__(self):
        return f'Pitches {self.title}'