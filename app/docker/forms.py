#coding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,Label,\
					FormField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError


class VolumesForm(Form):

	hostpath = StringField('hostpath',validators=[Required()])
	containerpath = StringField('containerpath',validators=[Required()])
	mode = SelectField('mode',choices=[('rw','rw'),('ro','ro')])


class ContainerForm(Form):
	name = StringField('name',validators=[
		Required(),Length(1,64),
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'name must have only letters, numbers, dots or underscores')])
	image = StringField('image',validators=[Required()])

	volumes = FormField(VolumesForm,label=None, validators=None, separator=u'-')
	start = BooleanField('start?')
	submit = SubmitField('Create')

	# def validate_name(self, field):
	# 	if Docker.query.filter_by(name=field.data).first():
	# 		raise ValidationError('Docker name already in use.')