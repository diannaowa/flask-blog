#coding=utf-8
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin
import bleach
from markdown import markdown
from . import db

from . import login_manager
import datetime

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(100))
    brief = db.Column(db.String(300))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
    content_html = db.Column(db.Text)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.content_html = bleach.linkify(bleach.clean(
                                markdown(value, output_format='html'),
                                tags=allowed_tags, strip=True))

db.event.listen(Posts.content, 'set', Posts.on_changed_body)  

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64),unique=True,index=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))