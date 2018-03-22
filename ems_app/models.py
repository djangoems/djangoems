from django.db import models

# Create your models here.
class organization(models.Model):
	name = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = 'Organization'

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