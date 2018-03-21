from django.db import models

# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length=100)

class Org_Branches(models.Model):
	org = models.ForeignKey(Organization, on_delete=models.CASCADE)
	branch_name = models.CharField(max_length=100)