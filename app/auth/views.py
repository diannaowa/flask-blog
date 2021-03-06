#coding=utf-8
from flask import render_template,redirect,request,url_for,flash
from flask.ext.login import login_user,login_required,logout_user

from . import auth
from ..models import User
from forms import LoginForm,RegisterForm

from .. import db

@auth.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		if user is not None and user.verify_password(form.password.data):
			login_user(user,form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))

		flash('Invalid username or password.')

	return render_template('auth/login.html',form = form)


@auth.route('/register',methods=['GET','POST'])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		user = User(username=form.username.data,password=form.password.data,email=form.email.data)
		db.session.add(user)
		flash('You can now login.')
		return redirect(url_for('.login'))

	return render_template('auth/register.html',form = form)


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have log out')
	return redirect(url_for('main.index'))