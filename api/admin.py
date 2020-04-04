from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .forms import SocioChangeForm, SocioCreationForm
from .models import Socio, Project, FeeDistribution, Fee


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
admin.site.register(Project)
admin.site.register(Fee)
admin.site.register(FeeDistribution)
