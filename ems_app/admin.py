from django.contrib import admin

# Register your models here.
from .models import organization, org_branches

class organizationAdmin(admin.ModelAdmin):
	class Meta:
		model = organization

admin.site.register(organization, organizationAdmin)

class org_branchesAdmin(admin.ModelAdmin):
	class Meta:
		model = org_branches

admin.site.register(org_branches, org_branchesAdmin)
