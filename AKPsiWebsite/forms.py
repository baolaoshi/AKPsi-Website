from django.contrib.auth.forms import UserCreationForm
from django import forms
from portal.models import Rushee

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 75:
            raise forms.ValidationError(u'Username must be shorter than 75 characters')
        return username

class NewRusheeForm(forms.ModelForm):
    class Meta:
        model = Rushee
        fields = ("phone_num", "dorm", "grad_class", "major", "gpa", "q1", "q2", "q3", "q4", "picture", "resume")