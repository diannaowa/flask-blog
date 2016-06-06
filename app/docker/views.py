#coding=utf-8
from flask import render_template,redirect,request,url_for,flash
from flask.ext.login import login_user,login_required,logout_user
import jinja2
from . import docker
from forms import ContainerForm
from utils import client
import json

@docker.route('/create_container',methods=['GET','POST'])
@login_required
def create_container():
	'''create container from an image,
		you can start it when create successful.
	'''
	if request.method == "POST":

		start = request.form['start']
		stat = client.create_and_start_container(
				name = request.form['name'],
				image = request.form['image'],
				expose = request.form['expose'],
				host_path = request.form['host_path'],
				container_path = request.form['container_path'],
				mode = request.form['mode'],
				host_port = request.form['host_port'],
				container_port = request.form['container_port']
			)

	images = client.get_images()

	return render_template('docker/create_container.html',images=images)


@docker.route('/containers',methods=['GET'])
@login_required
def show_containers():
	containers = client.get_containers(all=True)
	return render_template('docker/show_containers.html',containers=containers)


@docker.route('/container_detail/<string:c_id>',methods=['GET'])
@login_required
def container_detail(c_id):
	return c_id

@docker.route('/stop_container/<string:c_id>',methods=['GET'])
@login_required
def stop_container(c_id):
	client.stop_container(c_id)
	return json.dumps({'state':True})


@docker.route('/start_container/<string:c_id>',methods=['GET'])
@login_required
def start_container(c_id):
	client.run_container(c_id)
	return json.dumps({'state':True})

@docker.route('/remove_container/<string:c_id>',methods=['GET'])
@login_required
def remove_container(c_id):
	client.remove_container(c_id)
	return json.dumps({'state':True})


