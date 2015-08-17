import glob
import os

index=1
def db_deleter_main():
	global index
	filelist=glob.glob("/home/sys8/twitter/db/*_db")
	for f in filelist:
		os.remove(f)
		print "removing file " + str(index)
		index+=1
	return
