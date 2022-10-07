from .modelsBase import Base, sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin
from ws_config01 import ConfigDev, ConfigProd

config = ConfigDev()
    

class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    oura_token_id = relationship("Oura_token", backref="oura_token_id", lazy=True)
    oura_sleep = relationship('Oura_sleep_descriptions', backref='oura_sleep', lazy=True)
    loc_day = relationship('User_location_day', backref='user_loc_day', lazy=True)
    user_notes_ref = relationship('User_notes', backref='user_notes_ref', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def get_reset_token(self, expires_sec=1800):
        s=Serializer(config.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(config.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email})'

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    word_doc = Column(Text)
    notes = Column(Text)
    posts_to_html = relationship('Postshtml', backref='postDetails', lazy=True)
    posts_to_html_chars = relationship('Postshtmltagchars', backref='postDetailsChars', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"Posts(id: {self.id},blog_title: {self.title}, time_stamp_utc: {self.time_stamp_utc})"

class Postshtml(Base):
    __tablename__ = 'postshtml'
    id = Column(Integer, primary_key=True)
    word_row_id = Column(Integer)#this would be the dict_key if i were still using dict/json method
    row_tag = Column(Text)
    row_going_into_html = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)#table with MANY
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)#table with MANY
    posts_to_html_tag = relationship('Postshtmltagchars', backref='postChars', lazy=True)#table with ONE
    
    def __repr__(self):
        return f"Postshtml(id: {self.id}, word_row_id: {self.word_row_id} , " \
            f"row_tag: {self.row_tag}, row_going_into_html: {self.row_going_into_html})"

class Postshtmltagchars(Base):
    __tablename__ = 'postshtmltagchars'
    id = Column(Integer, primary_key=True)
    post_tag_characters = Column(Text)
    word_row_id = Column(Integer, ForeignKey(Postshtml.id), nullable=False)#table with MANY
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)#table with MANY

    def __repr__(self):
        return f"Postshtmltagchars(id: {self.id}, " \
            f"posts_to_html_id: {self.posts_to_html_id}, " \
            f"post_tag_characters: {self.post_tag_characters})"


class User_notes(Base):
    __tablename__ = 'user_notes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime_of_note=Column(DateTime)
    note_title = Column(Text) #walking, running, empty is ok for something like mood
    note_details = Column(Text)
    source_name=Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"User_notes({self.id},datetime_of_note:{self.datetime_of_note}," \
        f"note_title: {self.note_title}, note_details: {self.note_details}," \
        f"time_stamp_utc: {self.time_stamp_utc})"