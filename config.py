#config file for app
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['sevenunusual@gmail.com']
	POSTS_PER_PAGE = 3

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'kiss-my-ass'

	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ('sqlite:///' + os.path.join(basedir, 'app.db'))