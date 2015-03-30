from __future__ import print_function
from io import open

import requests
import sys, os
import re
from getpass import getpass

try:
	# Python 2
        prompt = raw_input
except NameError:
        # Python 3
        prompt = input


def get_file_size(filename):
	if os.path.exists(filename):
		size = os.stat(filename).st_size
		if size <= 0:
			raise ValueError('File size too small.')
		if size > 1*1024*1024*1024:
			raise ValueError('File is larger than 1GB.')
	else:
		raise OSError('No such file or directory: %s' %filename)	

def get_image_size(filename):
	if os.path.exists(filename):
		size = os.stat(filename).st_size
		if size <= 0:
			raise ValueError('File size too small.')
		if size > 30*1024*1024:
			raise ValueError('File is larger than 1GB.')
	else:
		raise OSError('No such file or directory: %s' %filename)	 

def read_file(infilename):#TODO: read files in chunks than load it all in memory
	try:
       		infile = open(infilename, 'rb')
       		content = infile.read()
       		infile.close()
       		return content
	except IOError as err:
		raise "Error reading file: %s"%err

def is_supported_image(image):
	supported_ext = ['gif', 'jpeg', 'png', 'bmp']
	image_ext = os.path.splitext(image)[1]
	if image_ext[1:] in supported_ext:
		return True
	else:
		return False

def get_link(html):
	r_ul = re.compile(r'\s*(?i)href\s*=\s*(\"([^"]*\")|"[^"]*"|([^"">\s]+))')
	link = re.findall(r_ul, html)
	return link[0][0]

class EZuploader():
	def __init__(self, filename=None):
		self.filename = filename
		self.host = 'upload.evilzone.org'
		self.url = 'http://{0}'.format(self.host)
		self.session = None
		
		self.agent = 'Mozilla/5.0 (X11; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0'
		self.type = 'multipart/form-data'
		self.referer = 'http://upload.evilzone.org/index.php?page=fileupload'
		
	def login(self):
		login_url = 'https://evilzone.org/login'
		username = prompt('Username for Evilzone.org: ')
		password = getpass('Password for Evilzone.org: ')
		print (username, password)
		self.session = requests.session()
		r = self.session.post(login_url, params={'username':username, 'password':password})
		if r.status_code == requests.codes.ok:
			return self.session
		else:
			return None
		
		
	def fileupload(self, filename=None):
		path = '/index.php?page=fileupload&filename={0}'
		filepath = filename or self.filename
		_filename = os.path.basename(filepath)
		file_url = self.url + path.format(_filename)
		self.size = get_file_size(filepath)
		self.headers = {'content-type': self.type, 'User-Agent': self.agent,
					'Referer': self.referer, 'Content-Length': self.size}	
		
		if self.session is not None:
			print('session in set')
			r = self.session.post(url=file_url, headers=self.headers, data=read_file(filepath))
			print ('Done')
		else:
			r = requests.post(url=file_url, headers=self.headers, data=read_file(filepath))
		if 'Error' not in r.text:
			return 'http://upload.evilzone.org?page=download&file='+r.text
		else:
			return None

	def imageupload(self, filename=None):
		path = '/index.php?page=imageupload&upload=true'
		imagepath = filename or self.filename
		image_url = self.url + path
		self.size = get_image_size(imagepath)
		self.headers = {'content-type': self.type, 'User-Agent': self.agent, 'Referer': self.referer, 'Content-Length': self.size}	
		if is_supported_image(imagepath):
			if self.session is not None:
				print('session in set')
				r = self.session.post(url=image_url, headers=self.headers, data=read_file(imagepath))
				print ('Done')
			else:
				print('session not set')
				r = requests.post(url=image_url, headers=self.headers, data=read_file(imagepath))
			if 'Error' not in r.text:
				return self.url + '/' + get_link(r.text).strip('"')
			else:
				return None
		else:
			raise TypeError("Image format not supported.")
