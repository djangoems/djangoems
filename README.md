# djangoems

New Migrations
======================

Follow these steps to create new migration:
1) python manage.py makemigrations
2) python manage.py showmigrations
3) python manage.py sqlmigrate ems_app "<migrationId>"
4) python manage.py migrate


Reset App Migrations
========================

python manage.py migrate ems_app zero


For plural and singular uses in Models
=======================================

Use verbose name in Meta class for respective Model as
Ex:
class organization(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = 'Organization'


Return Object for a Model
===============================

Use the below code to return an object of a model when the record is created for a model
Ex:
class organization(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = 'Organization'

	def __str__(self):
	    return self.name


Change Caption for an App
============================

1) Go to apps.py and add verbose_name for each AppConfig class
2) Go to init.py in app and add default_app_config = 'app.apps.configPath'
