from django.db import models
import datetime

class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters')
	slug = models.SlugField()
	description = models.TextField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"
	
	class Admin:
		pass
		
	#TODO: This does not work!
	#class CategoryAdmin(admin.ModelAdmin):
	    #prepopulated_fields = {"slug": ("title",)}
		
	def __unicode__(self):
		return self.title
		
	def get_absolulte_url(self):
		return "/categories/%s/" % self.slug		

class Entry(models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters')
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	slug = models.SlugField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Entries"
	
	class Admin:
		pass

	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return "/%s/%s" % (self.pub_date.strftime("%Y/%m/%d").lower(),self.slug)