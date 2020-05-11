from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Socio, USER_TYPES


class SocioCreationForm(UserCreationForm):
    # fee = forms.FloatField()
    # type = forms.Select(choices=USER_TYPES)

    # def save(self, commit=True):
    #     fee = self.cleaned_data.get('fee', None)
    #     type = self.cleaned_data.get('type', None)
    #     return super(Socio, self).save(commit=commit)

    class Meta(UserCreationForm.Meta):
        model = Socio
        #fields = UserCreationForm.Meta.fields + ('fee', 'type',)
        fields = ('username', 'email','fee')


class SocioChangeForm(UserChangeForm):
    # fee = forms.FloatField()
    # type = forms.Select(choices=USER_TYPES)

    # def save(self, commit=True):
    #     fee = self.cleaned_data.get('fee', None)
    #     type = self.cleaned_data.get('type', None)
    #     return super(Socio, self).save(commit=commit)

    class Meta:
        model = Socio
        fields = ('username', 'email','fee')