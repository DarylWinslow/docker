from os import listdir
from os.path import isfile, join

#function to return names of files in upload directory
def list_files():
        mypath = "/home/user/lab4/docker/python-flask/my_application/upload"
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	return 'Hello'

list_files()
