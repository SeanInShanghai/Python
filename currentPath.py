import sys
import os

def getCurrentPath():
	path = sys.path[0]
	
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)
print getCurrentPath()
