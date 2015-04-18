#!/usr/bin/env python

<<<<<<< HEAD
from distutils.core import setup
from setuptools import find_packages
import tempfile, shutil, os
=======

from setuptools import setup, find_packages
import tempfile
>>>>>>> d1ee2d88e363fffcb8babfd9be44c60e7e3c6996
import evilupload


requires = ['cookielib', 'requests', 'mechanize']

def do_setup():

	try:
		# This special screwing is to make main.py get installed to PATH as
        	# evilupload, not main.py. Don't remove it, or you'll break it.
	        tmp_dir = tempfile.mkdtemp()
        	tmp_main_script = os.path.join(tmp_dir, 'evilupload')
        	shutil.copy('main.py', tmp_main_script)

		with open('README.txt') as file:
    			long_description = file.read()
	
<<<<<<< HEAD
		setup(name='evilupload',
			version=evilupload.__version__,
			description='Functions and methods to upload files to Evilzone.org upload service.',
			author='Evilzone.org Community',
			author_email='kenjoe41.nafuti@gmail.com',
			long_description=long_description,
			url='https://www.evilzone.org',
			packages=find_packages(),
			scripts=[tmp_main_script],
			requires=requires,
			classifiers=[
        	  		"Intended Audience :: Developers",
        	  		"Natural Language :: English",
        	  		"Programming Language :: Python",
        	  		"Topic :: Internet :: WWW/HTTP",
        	  		"Topic :: Software Development :: Libraries :: Python Modules",
        	  		]
		)

	finally:
        	try:
            		shutil.rmtree(tmp_dir)
        	except OSError as e:
            		if e.errno != 2:  # The directory is already gone, so ignore it
                		raise
=======
	with open('README.txt') as file:
    		long_description = file.read()

	setup(name='evilupload',
		version=evilupload.__version__,
		description='Functions and methods to upload files to Evilzone.org upload service.',
		author='Evilzone.org Community',
		author_email='kenjoe41.nafuti@gmail.com',
		long_description=long_description,
		url='https://www.evilzone.org',
		packages=find_packages(),
		entry_points={
			'console_scripts': [
				'evilupload = evilupload.main:main',
			]
		},
		requires=requires,
		classifiers=[
          		"Intended Audience :: Developers",
          		"Natural Language :: English",
          		"Programming Language :: Python",
          		"Topic :: Internet :: WWW/HTTP",
          		"Topic :: Software Development :: Libraries :: Python Modules",
          		]
	)
>>>>>>> d1ee2d88e363fffcb8babfd9be44c60e7e3c6996

if __name__ == "__main__":
    do_setup()
