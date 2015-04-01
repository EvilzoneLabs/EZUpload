#!/usr/bin/env python

from distutils.core import setup
import tempfile


requires = ['cookielib', 'requests', 'mechanize']

def do_setup():

	
	with open('README.txt') as file:
    		long_description = file.read()

	setup(name='evilupload',
		version='1.1',
		description='Functions and methods to upload files to Evilzone.org upload service.',
		author='Evilzone.org Community',
		author_email='kenjoe41.nafuti@gmail.com',
		long_description=long_description,
		url='https://www.evilzone.org',
		packages=[str('evilupload')],
		requires=requires,
		classifiers=[
          		"Intended Audience :: Developers",
          		"Natural Language :: English",
          		"Programming Language :: Python",
          		"Topic :: Internet :: WWW/HTTP",
          		"Topic :: Software Development :: Libraries :: Python Modules",
          		]
	)

if __name__ == "__main__":
    do_setup()
