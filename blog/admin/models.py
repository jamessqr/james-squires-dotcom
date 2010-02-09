from google.appengine.ext import db
from django import newforms as forms

class Entry(db.Model):
	title = db.StringProperty()
	description = db.StringProperty()
	slug = db.StringProperty() #double check datatype
	created_on = db.DateTimeProperty()
	created_by = db.UserProperty()
	
	#TODO
	#Tags, categories