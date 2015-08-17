from simplejson import loads
import threading
import urllib2
import requests
import MySQLdb
import time
import twitterdump
import os
import dump_zipper
import db_deletion


proxy=urllib2.ProxyHandler({})
opener=urllib2.build_opener(proxy)
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
dic=OrderedDict()

#main_list=[]
start="737848638"
block= False
filetracker=open("/home/sys8/twitter/twitter_track.txt","a+")
temptracker=open("/home/sys8/twitter/temp_tracker.txt","a+")
dic[737848638]="https://twitter.com/legendstevejobs"

#def file_temp():
	

def id_Checker(user_id):
	global dic
	if user_id in dic.keys():
		return False
	else :		
		return True


count=0

def comeback():
	global block
	time.sleep(18000)
	block=False
	
	
def pagedownloader(user_id,user_url):
	url=urllib2.urlopen(user_url).read()
	user_name=user_url.split('/')[3]
	global count	
	filetracker.write(str(user_id)+"##"+str(user_url)+"##"+str(user_name)+"\n")
	temptracker.write(str(user_url)+"\n")
	count=count+1
	


def urlmaker(user_id,user_url):
	try:
		global dic
		global main_list
		global count
		global block
		
		r=requests.get("https://twitter.com/i/related_users/"+str(user_id))
		#print r.status_code
		if r.status_code==requests.codes.ok:
			
			pagedownloader(user_id,user_url)
			print user_url
			#count=count+1
			
			data=(loads(r.content))
			data=data.get('related_users_html')
			soup=bs(data)
			div=soup.findAll("div",{"class":"content"})
			for i in range(len(div)):
				#print "https://twitter.com"+div[i].find("a").get("href")
				user_id=div[i].find("a").get("data-user-id")
		
				check=id_Checker(user_id)
		
				if check:
					
					#main_list.append(div[i].find("a").get("data-user-id"))
					dic[div[i].find("a").get("data-user-id")]=str("https://twitter.com"+div[i].find("a").get("href"))
			
		else :
			print r.status_code
			block=True	
		#print dic
		#print main_list
	except Exception as exp:
		print "******************EXCEPTION********************************"
		print exp
		
		
urlmaker(737848638,"https://twitter.com/legendstevejobs")
index=1
zipper_index=1
while True:
	
	try :  

		
		if threading.activeCount()<5 and block == False:
			
			t=threading.Thread(target=urlmaker,args=(dic.keys()[index],dic.values()[index],))
			t.start()
			index=index+1
			print "count is :: "+str(index)
			if index%10000==0:

				print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
				print "                        SLEEPING                                  "
				print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" 
				temptracker.close()
				#time.sleep(100)
				twitterdump.dumper()
				print "Removing file : "
				os.remove("/home/sys8/twitter/temp_tracker.txt")
				print "File removed "
				temptracker=open("/home/sys8/twitter/temp_tracker.txt","a+")
				print "File Created Again "
				print "Zipper Started"
				dump_zipper.zipper_main(zipper_index)
				zipper_index+=1
				print "Db deletion starting..."
				db_deletion.db_deleter_main()
				print "indexing started again"
				#temptracker=open("/home/sys8/twitter/temp_tracker.txt","a+")
				
	
				print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
				print  "                       WAKE UP                                  "
				print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			else:
				continue
		else:
			comeback()
			
	except Exception as exp:
		print "@@@@@@@@@@@@@@@@@@@@@@@EXCEPTION@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"	
		print exp

