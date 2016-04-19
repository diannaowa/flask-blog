#coding=utf-8
from flask import render_template,session,redirect,url_for,flash

from . import main
from .forms import PostForm
from .. import db
from ..models import User,Posts

from flask.ext.login import login_required,current_user

@main.route('/',methods=['GET'])
def index():
	posts = Posts.query.order_by(Posts.timestamp.desc()).all()
	return render_template('index.html',posts = posts)


@main.route('/detail/<int:p_id>')
def detail(p_id):
	return 'Plz log in'


@main.route('/post',methods=['GET','POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Posts(title = form.title.data,content = form.content.data,author=current_user.username)
		db.session.add(post)
		flash('Post entry OK')
		#return redirect(url_for('.index'))
	return render_template('post.html',form=form)