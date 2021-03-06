from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from members.forms import RegistrationForm, MemberAutenticationForm, UpdateUserForm
from django.views.generic.edit import DeleteView
from members.models import Member
from django.contrib import messages

# Create your views here.

def delete_succes(request):
    return render(request, 'delete_succes.html', {})

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = MemberAutenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, ('Udało się zalogować!'))
                return redirect('home')
        else:
            messages.success(request, ('Nie udało się zalogować!'))
    else:
        form = MemberAutenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, ('Udało się wylogować!'))
    return redirect('home')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(request, ('Udało się zarejestrować!'))
            return redirect('home')
        else:
            messages.success(request, ('Nie udało się Zarejestrować!'))
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Udało się zaktualizować profil')
            return redirect(to='user_home')
        else:
            messages.success(request, 'Nie udało się zaktualizować profilu')
            return redirect(to='update')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'update.html', {'user_form': user_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Udało się zmienić hasło"
    success_url = reverse_lazy('user_home')

class CustomUserDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('delete_succes')