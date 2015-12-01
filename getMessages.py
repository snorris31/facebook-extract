import requests
import facebook
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import exc
#this is the method run to get all of the posts in a facebook group. 
#access token MUST be updated every few hours. 
#the 'requests' feature allows you to pull all that is in that particular url
def getMessages():
	token = "CAACEdEose0cBAEHcWK0Imh3h47E7Gf4hCERdw81sNvYVaAmvN3Wh0xEM9D2NzctTJc5Fkq5OQvC0Oc0fEVmYYSW3TaWl3j5ZAZAr5L469xHBPMpbHprjhNqagBBNolkTzeTmtTQqdLfJUhutZCwKyFmfPX0GyfBY9tpRaKqEAwTf3mPEb6NtOHnmF5IthSK0b9Ef5AGGQZDZD"
	params = {'access_token': token}
	r = requests.get("https://graph.facebook.com/v2.5/948104118584796/feed", params = params)
	return r.json()
#this is the method run to get all of the comments on posts in a facebook group. 
#access token MUST be updated every few hours. 
#the 'requests' feature allows you to pull all that is in that particular url
def getComments(str): 
    token = "CAACEdEose0cBAEHcWK0Imh3h47E7Gf4hCERdw81sNvYVaAmvN3Wh0xEM9D2NzctTJc5Fkq5OQvC0Oc0fEVmYYSW3TaWl3j5ZAZAr5L469xHBPMpbHprjhNqagBBNolkTzeTmtTQqdLfJUhutZCwKyFmfPX0GyfBY9tpRaKqEAwTf3mPEb6NtOHnmF5IthSK0b9Ef5AGGQZDZD"
    params = {'access_token' : token}
    #id = message['id']
    r = requests.get("https://graph.facebook.com/v2.5/" + str + "/comments" , params = params)
    return r.json()

def to_args(id=None, message=None, updated_time=None):
	print id, messages, None

def to_args(userfrom=None, message=None, created_time=None):
 	print id, message, userfrom, None

#this is the main method where the functions above are run. It calls the methods above and then stores it into its' respective table one by one.
#the try/except checks for all the posts/comments that are already in the table.
if __name__ == '__main__':
 	engine = create_engine('mysql://username:password@localhost/databasename')
 	facebook.Base.metadata.bind = engine
 	DBSession = sessionmaker(bind = engine)
 	session = DBSession()
 	response = getMessages()
 	for p in response['paging']:
 		for message in response['data']:
			comments = getComments(message['id'])
			record = facebook.FacebookPost(**message)
 			record.message = record.message.encode('utf8')
 			session.add(record)
			try:
				session.commit()
			except UnicodeEncodeError as e:
				session.rollback()
				print e
			except exc.IntegrityError as e:
				session.rollback()
				print 'item already exists'
			for comment in comments['data']:
				fields = {'id': comment['id'],
					  	'userfrom': comment['from']['name'],
					  	'created_time': comment['created_time'],
					  	'message': comment['message']}
				record = facebook.FacebookComment(**fields)
				record.message = record.message.encode('utf8', errors='ignore')
				session.add(record)
				try:
					session.commit()
				except UnicodeEncodeError as e:
					session.rollback()
					print e
				except exc.IntegrityError as e:
					session.rollback()
					print 'item already exists'
