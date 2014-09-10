# Django Blog Running on Appengine - Non-rel DB

This is a basic Blog using Django and configured for Google Appengine with a non-relational database.  Please note that I hacked this together at the time of the Appengine release as an exercise to get it working.  To get things working requires a magic combination of versions as of this writing.

## Development Setup

To get things running locally you need to first download the Google App Engine Launcher 1.7.4 - https://console.developers.google.com/storage/appengine-sdks/deprecated/174/

	$ brew install python
	$ git clone thisrepo
	$ git submodule init
	$ git submodule update

Setup Symlinks

	$ ln -s ~/PATHTOPROJECT/lib/djangoappengine/ ~/PATHTOPROJECT/djangoappengine
	$ ln -s ~/PATHTOPROJECT/lib/dbindexer/dbindexer/ ~/PATHTOPROJECT/dbindexer
	$ ln -s ~/PATHTOPROJECT/lib/django-nonrel/django/ ~/PATHTOPROJECT/django
	$ ln -s ~/PATHTOPROJECT/lib/djangotoolbox/djangotoolbox/ ~/PATHTOPROJECTdjangotoolbox

Launch the Google App Engine Launcher to ensure that it creates the necessary symlinks for the binaries

Configure a super user for the admin

	$ python manage.py createsuperuser --username=username --email=asdf@asdf.com

Run the App (Note: Do not use the app engine launcher directly, only use it for deployment)

	$ python manage.py runserver

Open a Browser to Checkout the Site! - http://127.0.0.1:8000