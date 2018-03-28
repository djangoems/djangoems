from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class organization(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = ' Organization'
		verbose_name_plural = ' Organization'

	def __str__(self):
	    return self.name

class org_branches(models.Model):
	org = models.ForeignKey(organization, on_delete=models.CASCADE)
	branch_name = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Branch'
		verbose_name_plural = 'Branches'

	def __str__(self):
	    return self.branch_name

class user_profile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	branch = models.ForeignKey(org_branches, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Profile'

class classes(models.Model):
	class_name = models.CharField(max_length=30)
	branch = models.ForeignKey(org_branches,on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Class'
		verbose_name_plural = 'Classes'

	def __str__(self):
		return self.class_name

class sections(models.Model):
	section_name = models.CharField(max_length=30)
	clas = models.ForeignKey(classes,on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Section'
		verbose_name_plural = 'Sections'

	def __str__(self):
		return self.section_name