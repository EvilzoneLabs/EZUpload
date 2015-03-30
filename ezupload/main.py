import sys

import evilzone

def main(argc, argv):
	
	ezup = evilzone.EZuploader()
	ezup.login()
	url = ezup.fileupload(argv[1])
	print url

if __name__ == "__main__":
    	sys.exit(main(len(sys.argv), sys.argv))
