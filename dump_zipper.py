import shutil
def zipper_main(i):
	shutil.make_archive("output"+str(i),'zip',"/home/sys8/twitter/db")
	return

