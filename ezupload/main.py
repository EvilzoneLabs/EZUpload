import sys

import evilzone

def main(argc, argv):
	print argv[1]
	ezup = evilzone.EZuploader()
	url = ezup.imageupload(argv[1])
	print url

if __name__ == "__main__":
    	sys.exit(main(len(sys.argv), sys.argv))
