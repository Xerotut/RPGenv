from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME


def registration_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "accounts/registration_page.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get(REDIRECT_FIELD_NAME)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("mythic:games_page")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, "accounts/login_page.html", context)

# Create your views here.
