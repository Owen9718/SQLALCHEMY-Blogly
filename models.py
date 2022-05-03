"""Models for Blogly."""

# from msilib.schema import Class

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL ="https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    image_url = db.Column(db.Text, nullable=False, default= DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"