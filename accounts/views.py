from django.shortcuts import render, redirect
from .models import Account, Profile, Company, Division, Position
from .forms import RegistrationForm, EditProfileForm, EditUserForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import re
import os

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name'] 
            last_name = form.cleaned_data['last_name'] 
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration success !! ')
            return redirect('register')
        else:
            messages.warning(request, 'Something bad happend, Try again!!')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None and user.is_active == True:
            auth.login(request, user)
            messages.success(request,'Succesfully Login')
            return redirect('home')
        else:
            messages.warning(request, 'Email or Password Invalid Try Again')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You successfully logout !!')
    return redirect('login')



@login_required(login_url='login')
def profile(request):
    userprofile = get_object_or_404(Profile, user=request.user)
    company_list = Company.objects.all()
    division_list = Division.objects.all()
    position_list = Position.objects.all()
    user = get_object_or_404(Account, email=request.user.email)
    
    if request.method == 'POST':
        form_id = request.POST['form_identifier']
        if form_id == "form_profile":
            user_form = EditUserForm(request.POST, instance=request.user)
            profile_form = EditProfileForm(request.POST, request.FILES, instance=userprofile)
            user_company = request.POST['company']
            user_division = request.POST['division']
            user_position = request.POST['position']
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                user = Profile.objects.get(user=request.user)
                #validate to handle empty input
                if user_company == 'None':
                    user_company = None
                else:   
                    user.company = Company.objects.get(company_name=user_company)
                
                if user_division == 'None':
                    user_division == None
                else:
                    user.division = Division.objects.get(division_name=user_division)
                
                if user_position == 'None':
                    user_position = None
                else:
                    user.position = Position.objects.get(position_name=user_position)
                user.save()
                messages.success(request, 'Profile updated succesfully !! ')
            else:
                messages.error(request, "Invalid Input, Try Again")
        if form_id == "form_password":
            password = request.POST['password']
            if user.check_password(password) == False:
                messages.warning(request, 'Wrong password')
            else:
                newpassword = request.POST['newpassword']
                renewpassword = request.POST['renewpassword']
                
                if newpassword != renewpassword:
                    messages.warning(request, "Password not match, try again")
                #check if password strong enough using regex :)
                if is_strong_password(newpassword):
                    user.set_password(newpassword)
                    user.save()
                    messages.success(request, 'Password successfully updated')
                else:
                    messages.warning(request, "Password too weak !")                     

    user_form = EditUserForm(instance=request.user)
    profile_form = EditProfileForm(instance=userprofile)
    
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'company_list' : company_list,
        'division_list' : division_list,
        'position_list' : position_list,
    }
    return render(request, 'accounts/profile.html', context)

#password checker using regex int
def is_strong_password(password):
    # Define the regular expression for a strong password
    regex = (
        r'^(?=.*[a-z])'  # At least one lowercase letter
        r'(?=.*[A-Z])'   # At least one uppercase letter
        r'(?=.*\d)'      # At least one digit
        r'[\w\d!@#$%^&*()-_=+{};:,<.>]{8,}$'  # Minimum length 8 and allowed special characters
    )
    return bool(re.match(regex, password))

#remove profile image
def remove_profile_image(request):
    userprofile = Profile.objects.get(user=request.user)
    image_path = userprofile.profile_picture.path
    # Delete the image file
    if os.path.exists(image_path):
        os.remove(image_path)
    
    userprofile.profile_picture = None
    userprofile.save()
    
    return redirect(request, 'profile')