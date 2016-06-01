#coding=utf-8
from flask import render_template,session,redirect,url_for,flash,request,current_app

from . import main
from .forms import PostForm
from .. import db
from ..models import User,Posts

from flask.ext.login import login_required,current_user

@main.route('/',methods=['GET'])
def index():
	page = request.args.get('page', 1, type=int)
	pagination = Posts.query.order_by(Posts.timestamp.desc()).paginate(
			page, per_page=current_app.config['POSTS_PER_PAGE'],
			error_out=False)
	
	posts = pagination.items

	return render_template('index.html',posts = posts,pagination=pagination)


@main.route('/detail/<int:p_id>')
def detail(p_id):

	post = Posts.query.filter_by(id=p_id).first()
	if post is None:
		return render_template('404.html'),404
	return render_template('detail.html',post = post)


@main.route('/post',methods=['GET','POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Posts(title = form.title.data,brief=form.brief.data,content = form.content.data,author=current_user.username)
		db.session.add(post)
		flash('Post entry OK')
		#return redirect(url_for('.index'))
	return render_template('post.html',form=form)



@main.route('/edit/<int:p_id>',methods=['GET','POST'])
@login_required
def edit(p_id):
	post = Posts.query.filter_by(id=p_id).first()
	if post is None:
		return render_template('404.html'),404
	form = PostForm()

	if form.validate_on_submit():
		post.title = form.title.data
		post.brief = form.brief.data
		post.content = form.content.data
		db.session.add(post)
		flash('Edit entry OK')

	form.title.data = post.title
	form.brief.data = post.brief
	form.content.data = post.content
	return render_template('edit.html',post=post,form=form)


@main.route('/del/<int:p_id>')
@login_required
def delete(p_id):
	post = Posts.query.filter_by(id=p_id).first()
	db.session.delete(post)
	flash('Delete entry OK')
	return redirect(url_for('.index'))