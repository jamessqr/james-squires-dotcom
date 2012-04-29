from google.appengine.ext import db
from django import newforms as forms
import datetime

class Entry(db.Model):
	title = db.StringProperty()
	description = db.TextProperty()
	slug = db.StringProperty() #double check datatype
	created_on = db.DateTimeProperty(auto_now="true")
	created_by = db.UserProperty(auto_current_user="true")
	
	#TODO
	#Tags, categories