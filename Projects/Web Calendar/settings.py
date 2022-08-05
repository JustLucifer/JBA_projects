import os

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/events.db'

key = os.urandom(24)
SECRET_KEY = key
