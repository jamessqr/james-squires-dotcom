Django Appengine Blog - Non-rel
===============================

This is a basic Blog using Django and configured for Google Appengine with a non-relational database.

Installation
------------

1. Download and install Python 2.7
2. Download GAE (Note: the Django-nonrel project is not normally up to the latest GAE, the latest could cause blowouts)
3. Pull this git repo
4. Setup the submodules - submodule init
5. Pull the submodules - submodule update
3. Setup symlinks:
	* ln -s /path/to/project/lib/djangoappengine/ /path/to/project/djangoappengine
	* ln -s /path/to/project/lib/dbindexer/dbindexer/ /path/to/project/dbindexer
	* n -s /path/to/project/lib/django-nonrel/django/ /path/to/project/django
	* ln -s /path/to/project/lib/djangotoolbox/djangotoolbox/ /path/to/project/djangotoolbox
4. Configure a superuser for the admin - python manage.py createsuperuser --username=username --email=asdf@asdf.com
5. Run the application - python manage.py runserver
