import requests
import mysql.connector
class facebook:
	def __init__ (self, url) :
		self = self
		self.url = url
	
	def createPostObject(url):
		r = requests.get(url)
		cnx = mysql.connector.connect(user = Sara, password = middle96, database = 'facebookextract')
        cursor = cnx.cursor()
		for posts in r:
			add_data = ("INSERT INTO facebookextract "
        		"(posts[0], posts[1], posts[2])")

    		cursor.execute(add_data)
    		cnx.commit()
    	cnx.close()


