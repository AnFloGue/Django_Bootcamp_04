from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

# Create your views here.

User = get_user_model()


def register_view(request):
    """
    A view function for user registration. It processes the registration form data, creates a new user if the form is valid, logs in the user, and redirects to the homepage. If the user creation fails, it sets a session variable 'register_error' to 1.

    Parameters:
    - request: HttpRequest object containing metadata about the request
    """
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1  # 1 == True
    return render(request, "forms.html", {"form": form})


def login_view(request):
    """
    A view function for user login. It processes the login form data, authenticates the user, logs in the user if authentication is successful, and redirects to the homepage. If authentication fails, it sets a session variable 'invalid_user' to 1.

    Parameters:
    - request: HttpRequest object containing metadata about the request
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1  # 1 == True

    return render(request, "forms.html", {"form": form})


def logout_view(request):
    """
    Logs out the user and redirects them to the login page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the login page.
    """
    logout(request)
    return redirect("/login")
