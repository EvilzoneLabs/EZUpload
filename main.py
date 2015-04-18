import sys

from evilupload.evilupload import evilupload

def main(argc, argv):
	
	ezup = evilupload()
	ezup.login()
	#url = ezup.fileupload(argv[1])
	ezup.delete(argv[1])

if __name__ == "__main__":
    	sys.exit(main(len(sys.argv), sys.argv))
