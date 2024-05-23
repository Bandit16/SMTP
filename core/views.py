from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *


def homepage1(request):
    if request.user.is_authenticated:
        user = request.user
        if hasattr(user, 'profile'):
            profile = user.profile
            return HttpResponse('you are a perosnal profile')
        elif hasattr(user, 'organizationprofile'):
            organization_profile = user.organizationprofile
            return HttpResponse('you are a organization profile')
        else:
            return HttpResponse('error')

    else:
        # Redirect to a login page or handle anonymous users
        return HttpResponse('Please log in to view this page.')
def homepage(request):
    return render(request,'home.html')

# def accountSettings(request):
#     user = request.user
#     profile = None
#     org_profile = None
#     form_class = None
#     instance = None

#     # Check which profile the user has
#     try:
#         profile = Profile.objects.get(user=user)
#         form_class = MemberForm
#         instance = profile
#     except Profile.DoesNotExist:
#         profile = None

#     try:
#         org_profile = OrganizationProfile.objects.get(user=user)
#         form_class = OrganizationForm
#         instance = org_profile
#     except OrganizationProfile.DoesNotExist:
#         org_profile = None

#     if not form_class:
       
#         return HttpResponse('some_error_page')  

#     if request.method == 'POST':
#         form = form_class(request.POST, request.FILES, instance=instance)
#         # add request.user.username at form
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = form_class(instance=instance)

#     context = {
#         'form': form
#     }
#     return render(request, 'account_setting.html', context)
def accountSettings(request):
    user = request.user
    profile = None
    org_profile = None
    form_class = None
    instance = None

    # Attempt to retrieve profile based on user type
    try:
        profile = Profile.objects.get(user=user)
        form_class = MemberForm
        instance = profile
    except Profile.DoesNotExist:
        pass

    try:
        org_profile = OrganizationProfile.objects.get(user=user)
        form_class = OrganizationForm
        instance = org_profile
    except OrganizationProfile.DoesNotExist:
        pass

    if not profile and not org_profile:
        return HttpResponse('You need to create a profile.')

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = form_class(instance=instance)
        # Add user's username to the form
        form.fields['username'].initial = user.username  # Assuming 'username' is a field in your form

    context = {'form': form}
    return render(request, 'account_setting.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


def explore(request):
    return render(request,'explore.html')