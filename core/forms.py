
from .models import Profile,OrganizationProfile
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class MemberForm(ModelForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = Profile
        fields = ['phone', 'locaiton', 'profile_pic']
        exclude = ['user']

class OrganizationForm(ModelForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = OrganizationProfile
        fields = '__all__'
        exclude = ['user','name']


class CreateUserForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('organization', 'Organization'),
    )

    
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    location = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type','location']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_type = self.cleaned_data['user_type']
            location = self.cleaned_data['location']
            if user_type == 'personal':
                Profile.objects.create(user=user, locaiton=location)
            elif user_type == 'organization':
                OrganizationProfile.objects.create(user=user, locaiton=location)
        return user
