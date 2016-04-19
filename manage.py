#!/usr/bin/env python
#coding=utf-8
import os
from app import create_app,db
from app.models import User,Posts
from flask.ext.script import Manager
from flask.ext.migrate import Migrate,MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
	manager.run()