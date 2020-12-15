from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages, auth
from manager_app.forms import UserLoginForm, UserRegisterForm
from django.views.generic.edit import CreateView

class CreateUserView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/signup.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get("password"):
            user.set_password(form.cleaned_data.get("password"))
        user.save()
        return super(CreateUserView, self).form_valid(form)


def user_registration(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('in valid')
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            print(password)
            user.set_password(password)
            user.is_manager = True
            user.save()
            print(form.errors)
            messages.success(request, 'Account Created Successfully')
            return redirect('/')
        else:
            print("Errors")
            print(form.errors)
            messages.error(request, form.errors)
            return render(request, 'users/signup.html', {'form': form})
    return render(request, 'users/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': UserLoginForm})

    def post(self, request):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get['email']
            password = form.cleaned_data.get['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                if user.is_manager:
                    return redirect('/home')
                else:
                    print('in user exist error')
                    messages.error(request, "Username Or Password is incorrect.")
                    return redirect('login')
            else:
                messages.success(request, 'Incorrect Username Or Password')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect Username Or Password')
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('login')