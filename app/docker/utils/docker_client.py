#coding=utf-8

from docker import Client

class Dclient(object):

	def __init__(self):
		'''create a connection instance
		'''
		self.cli = Client(base_url='unix://run/docker.sock')

	def get_images(self):
		'''same to `docker images`
		'''
		return self.cli.images()


	def create_and_start_container(self,image,name,expose=None,host_port=None,container_port=None,host_path=None,
		container_path=None,mode=None
		):
		'''create and start container
		'''

		param,host_config = self.__create_container_args(image=image,name=name,expose=expose,host_port=host_port,
											container_port=container_port,host_path=host_path,
											container_path=container_path,mode=mode
											)
		config = {}
		host = None
		ports = None

		if param.has_key('ports'):
			ports = param['ports']

		if host_config.has_key('port_bindings'):
			config['port_bindings'] = host_config.get('port_bindings')

		if host_config.has_key('binds'):
			config['binds'] = host_config.get('binds')

		if config != {}:
			host = self.cli.create_host_config(**config)



		con = self.cli.create_container(image=param['image'],name=param['name'],
				ports=ports,host_config=host
				)


		if con.has_key('Id'):
			self.run_container(con.get('Id'))
			return True
		#
		return False


	def __create_container_args(self,**kwargs):

		param = {
			'image':kwargs['image'],
			'name':kwargs['name']
		}

		if kwargs['expose'] !='':
			param['ports'] = [(kwargs['expose'],'tcp')] #just support tcp
				
		port_bindings = None
		binds = None
		host_config = {}

		if kwargs['container_port'] != '' and kwargs['host_port'] != '':
			port_bindings = {kwargs['container_port']:kwargs['host_port']}

		if kwargs['container_path'] != '' and kwargs['host_path'] != '':

			binds = {kwargs['host_path']:{'bind':kwargs['container_path'],'mode':kwargs['mode']}}

		if port_bindings is not None:

			host_config['port_bindings'] = port_bindings


		if binds is not None:

			host_config['binds'] = binds


		return param,host_config


	def get_containers(self,all=False,trunc=True):
		'''Show all containers. Only running containers are shown by default
		'''
		return self.cli.containers(all=all)


	def stop_container(self,container_id):

		return self.cli.stop(container_id)


	def remove_container(self,container_id):
		return self.cli.remove_container(container_id)


	def run_container(self,container_id):
		return self.cli.start(container=container_id)
