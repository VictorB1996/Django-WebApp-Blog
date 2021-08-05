from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create Register View
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created. You can log in now!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        # We're instanciating these classes with that params because we want the 
        # fields to be populated with the information of the user currently logged in
        user_form = UserUpdateForm(request.POST, instance = request.user) # currently logged in user
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) # currently logged in user's profile

        if user_form.is_valid() and profile_update_form.is_valid():
            user_form.save()
            profile_update_form.save()
            messages.success(request, f"Your Profile has been succesfully updated!")
            return redirect("profile")

    else:
        user_form = UserUpdateForm(instance = request.user) # currently logged in user
        profile_update_form = ProfileUpdateForm(instance = request.user.profile) # currently logged in user's profile

    context = {
        "user_form": user_form,
        "profile_update_form": profile_update_form
    }

    return render(request, "users/profile.html", context)
