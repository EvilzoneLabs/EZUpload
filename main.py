from __future__ import print_function
import sys, os

from evilupload.evilupload import evilupload
from evilupload.evilupload import is_supported_image

def main(argc, argv):
	if argc < 1:
		print('Usage: evilupload file1, file2, .....')
		exit()
	
	ezup = evilupload()
	def upload(filename):
		if is_supported_image(filename):
			try:
				return ezup.imageupload(filename)
			except ValueError as e:#file is too big, lets put in the files folder instead
				return ezup.fileupload(filename)
		else:
			return ezup.fileupload(filename)

	lg = ezup.login()
	if lg is not None:
		print('Logged in')
	else:
		print('Login failed. Exiting...!')
		exit()
	
	uploaded_files = dict()
	for filepath in argv:
		filenm = os.path.basename(filepath)
		print ('Uploading: %s...' %filenm)
		url = upload(filepath)
		uploaded_files[filenm] = url
		
	print('Done')#All files are done
	
	for filename, url in uploaded_files.iteritems():
		print('%s: %s' %(filename, url))


if __name__ == "__main__":
    	sys.exit(main(len(sys.argv[1:]), sys.argv[1:]))
