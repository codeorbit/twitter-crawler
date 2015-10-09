# twitter-crawler
Crawl all the profiles of twitter user and make a html document of each user for further extraction of data
This module has four sub modules:

1.) twittermain.py :- This module will be used to crawl the links in the batch of 10000 links.
                      it consist of four functions :
                      
                      
                      1.1) id_checker : - this will make sure the only unique ids will be inserted into queue.
                      
                      1.2) comeback :- if block = true then program will go to sleep for 5 hours, will comeback after                             that.
                      
                      1.3) pagedownloader :- it will keep track of the links which has been extracted from the ids.
                      
                      1.4) urlmake :- it will make the url from the given ids.
                      
2.) twitterdump.py :- This module will crawl the main page of the link through dumper function and put them in a db 
                      folder.
                      
3.) dump_zipper.py :- This module will make the zip file of the dump created by the dumper function of the                                twitterdump.py.

4.) db_deletion.py :- Once the zip file is made of all the files present in db, this module will delete the files                        in db.
                      
                  
                      
