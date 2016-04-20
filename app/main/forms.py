#coding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from flask.ext.pagedown.fields import PageDownField


class PostForm(Form):

	title = StringField('Title',validators=[Required()])
	brief = TextAreaField('brief',validators=[Required()])
	content = PageDownField('Content',validators=[Required()])
	submit = SubmitField('Submit')