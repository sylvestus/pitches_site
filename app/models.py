
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


 
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    pitch = db.relationship('Pitches', backref='author', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(comment_id=id).all()
        return comments
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}' 



class Pitches(db.Model):

    __tablename__ = 'pitches_table'

    id = db.Column(db.Integer,primary_key = True)
    # pitch_id = db.Column(db.Integer)
    title = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    comment =db.relationship('Comments', backref='pitch', lazy='dynamic')
    
    # new_pitch= pitches_table(pitch_id="",pitch_title="interview",pitch_category="interview",the_pitch="hello iam ian",posted="",user_id="",comment="")


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        pitches= Pitches.query.filter_by(category=category).all()
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



class Comments(db.Model):

    __tablename__ = 'comments'

    id= db.Column(db.Integer,primary_key = True)
    # comment_id = db.Column(db.Integer)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches_table.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls,id):

        comments = Comments.query.order_by(Comments.posted).filter_by(pitches_id=id).all()
        return comments

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))




    


