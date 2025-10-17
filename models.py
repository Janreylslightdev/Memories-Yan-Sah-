from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    albums = db.relationship('Album', backref='user', lazy=True)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cover_image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=True)
    images = db.relationship('Image', backref='album', lazy=True, foreign_keys='Image.album_id')
    cover_image = db.relationship('Image', foreign_keys=[cover_image_id], uselist=False)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), nullable=False)
    original_filename = db.Column(db.String(150), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
