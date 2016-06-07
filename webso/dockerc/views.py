#coding=utf-8
from flask import render_template,redirect,request,url_for,flash
from . import ws

import time,json
from docker import Client

client = Client(base_url='unix://run/docker.sock')

@ws.route('/echo')
def echo_socket(socket):
    while not socket.closed:
        message = socket.receive()
        if message != '':
        	for i in range(10):
        		socket.send(message+':'+str(i))
        		time.sleep(1)



@ws.route('/pull')
def pull_images(socket):
	while not socket.closed:
		image = socket.receive()
		if image == '':
			socket.send('Please tell me which image you want to pull.')
		else:
			im = image.split(':')
			if im[1] == '':
				image += 'latest'
			for line in client.pull(image, stream=True):
				socket.send(json.dumps(json.loads(line), indent=4))