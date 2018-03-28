from django.contrib import admin

# Register your models here.
from .models import organization, org_branches, user_profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class organizationAdmin(admin.ModelAdmin):
	class Meta:
		model = organization

	def has_add_permission(self, request):
	    # if there's already an entry, do not allow adding
	    count = organization.objects.all().count()
	    if count == 0:
	      return True
	    return False
	    
admin.site.register(organization, organizationAdmin)

class org_branchesAdmin(admin.ModelAdmin):
	class Meta:
		model = org_branches

admin.site.register(org_branches, org_branchesAdmin)

class user_ProfileInline(admin.StackedInline):
	model = user_profile
	can_delete = False
	# verbose_name_plural = 'Profile'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (user_ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)