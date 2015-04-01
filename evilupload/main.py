import sys

import evilupload

def main(argc, argv):
	
	ezup = evilupload.EZuploader()
	print ezup.login()
	url = ezup.imageupload(argv[1])
	print url

if __name__ == "__main__":
    	sys.exit(main(len(sys.argv), sys.argv))
