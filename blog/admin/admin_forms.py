from django import newforms as forms
import models
from google.appengine.ext.db import djangoforms

class EntryForm(djangoforms.ModelForm):
	class Meta:
		model = models.Entry
