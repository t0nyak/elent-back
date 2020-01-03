from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

# from .forms import SocioChangeForm, SocioCreationForm
# from .models import Socio


# class SocioAdmin(UserAdmin):
#     add_form = SocioCreationForm
#     form = SocioChangeForm
#     model = Socio
#     list_display = ['email', 'username', 'fee',]
    # fieldsets = (
    #     (('User'), {
    #         'fields': ('fee', 'type',),
    #     }),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'fee', 'type','password1', 'password2',),
    #     }),
    # )
