from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SocioChangeForm, SocioCreationForm
from .models import Socio, Project, FeeDistribution, Fee, Image


class SocioAdmin(UserAdmin):
    add_form = SocioCreationForm
    form = SocioChangeForm
    model = Socio
    list_display = ['email', 'username', 'fee',]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'fee', 'type')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'fee', 'type','password1', 'password2',),
        }),
    )


admin.site.register(Socio, SocioAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit', 'visible', 'got', 'goal', 'created_on']


admin.site.register(Project, ProjectAdmin)


class FeeAdmin(admin.ModelAdmin):
    list_display = ['amount']


admin.site.register(Fee, FeeAdmin)


class FeeDistributionAdmin(admin.ModelAdmin):
    list_display = ['fee', 'project', 'percentage']


admin.site.register(FeeDistribution, FeeDistributionAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


admin.site.register(Image, ImageAdmin)
