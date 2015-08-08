from simplejson import loads
import threading
import urllib2
import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
dic=OrderedDict()
#fileopen=file("/home/akhil/Desktop/json.json","r")
main_list=[]
start="737848638"

dic[737848638]="https://twitter.com/legendstevejobs"
def id_Checker(user_id):
	global dic
	if user_id in dic.keys():
		return False
	else :		
		return True
def pagedownloader(dic_value):
	url=urllib2.urlopen(dicvalue).read()
	filename="%s_db.txt"%dic_value
	fileopen=open(filename,"w")
def urlmaker(user_id,user_value):
	try:
		global dic
		global main_list
		
		r=requests.get("https://twitter.com/i/related_users/"+str(user_id))
		print r.status_code
	
		print user_value
		data=(loads(r.content))
		data=data.get('related_users_html')
		soup=bs(data)
		div=soup.findAll("div",{"class":"content"})
		for i in range(len(div)):
			#print "https://twitter.com"+div[i].find("a").get("href")
			user_id=div[i].find("a").get("data-user-id")
		
			check=id_Checker(user_id)
		
			if check:
				main_list.append(div[i].find("a").get("data-user-id"))
				dic[div[i].find("a").get("data-user-id")]=str("https://twitter.com"+div[i].find("a").get("href"))
			
	
		#print dic
		#print main_list
	except Exception as exp:
		print "******************EXCEPTION********************************"
		print exp
		
		
urlmaker(dic.keys()[0],dic.values()[0])
index=0

while True:
	
	try :
		if threading.activeCount()<100:
			print "count is :: "+str(index)
			threading.Thread(target=urlmaker,args=(dic.keys()[index],dic.values()[index],)).start()
			index=index+1
	except Exception as exp:
		print "@@@@@@@@@@@@@@@@@@@@@@@EXCEPTION@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"	
		print exp

