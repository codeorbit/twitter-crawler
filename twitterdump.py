import urllib2
import threading
import timeit
import os
import time 
file_count =1
def dumper():

	try:
		dumper_file=file("/home/sys8/twitter/temp_tracker.txt","r")
		x=dumper_file.readlines()
		count=len(x)
		print count
		index =0
		#start = timeit.default_timer()

		#Your statements here


		def dumper(l):
		#for i in x:
			#print i

			url=urllib2.urlopen(l).read()
			user_name=l.split('/')[3]
			filename="%s_db"%user_name
			fileopen=open("/home/sys8/twitter/db/"+str(filename),"a+")
			fileopen.write(url)

		#stop = timeit.default_timer()


		while index<count:
			while threading.activeCount()<5:
				print "downloading : "+str(index)
				t=threading.Thread(target=dumper,args=(x[index],))
				t.start()
				index=index+1
		
		
		#time.sleep(500)
		#file_count=file_count+1
		return 
	except:
		pass
