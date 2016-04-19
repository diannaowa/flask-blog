#coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SECRET_KEY='hahahhaah'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass



class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI="mysql://root:123456@localhost:3306/blog?charset=utf8"



class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI="mysql://root:123456@localhost:3306/blog?charset=utf8"




config = {
	'development':DevelopmentConfig,
	'production':ProductionConfig,

	'default':DevelopmentConfig
}