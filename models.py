from datetime import datetime
from exts import db

class UserModel(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    join_time=db.Column(db.DateTime,default=datetime.now)

class Email_yanzhen(db.Model):
    __tablename__='email_yanzhen'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    yanzhenma=db.Column(db.String(100),nullable=False)

class QuestionModel(db.Model):
    __tablename__='question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)


    author_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    author=db.relationship(UserModel,backref="questions")

    filename=db.Column(db.String(255))

class AnwserModel(db.Model):
     __tablename__ = 'answer'
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     content = db.Column(db.Text, nullable=False)
     create_time = db.Column(db.DateTime, default=datetime.now)

     #外键
     question_id=db.Column(db.Integer,db.ForeignKey("question.id"))
     author_id=db.Column(db.Integer,db.ForeignKey("user.id"))

     #定义外键关系
     question=db.relationship(QuestionModel,backref=db.backref("answers",order_by=create_time.desc()))
     author=db.relationship(UserModel,backref="answers")

     author_name = db.Column(db.String(100))
     filename = db.Column(db.String(255))




