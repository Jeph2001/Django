from django.shortcuts import render
from .forms import SignupForm, LoginForm, ResetForm, KeepResetForm
from django.http import HttpResponseRedirect
from .models import SignUp
# Create your views here.

def confirming(request):
    return render(request, 'confirmation.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/confirm/')
    else:
        form = SignupForm()
    return render(request, 'sign_up.html', {'form': form})


def save_reset(request):
    if request.method == 'POST':
        kform = KeepResetForm(request.POST)
        if kform.is_valid():
            kform.save()
            return HttpResponseRedirect('/accounts/confirm/')
    else:
        kform = KeepResetForm()
    return render(request, 'reset_page.html', {'kform': kform})


# def login(request):
#     if request.method == 'POST':
#         lform = LoginForm(request.POST)
#         if lform.is_valid():
#             lform.save()
#             return HttpResponseRedirect('/accounts/confirm/')
#     else:
#         lform = LoginForm()
#     return render(request, 'login.html', {'lform': lform})

def login(request):
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = lform.cleaned_data['username']
            password = lform.cleaned_data['password']
            try:
                user = SignUp.objects.get(username=username)
                if user.password ==password:
                    return HttpResponseRedirect('/web_app/app/')
                else:
                    lform.add_error(None, "Incorrect password or username. we don't know you")
            except SignUp.DoesNotExist:
                lform.add_error(None, 'you seemed to be unkown in our system')
    else:
        lform = LoginForm()
    return render(request, 'login.html', {'lform': lform})


def password_reset(request):
    pform = ResetForm()
    if request.method == 'POST':
        pform = ResetForm(request.POST)
        if pform.is_valid():
            email_address = pform.cleaned_data['email_address']
            try:
                user = SignUp.objects.get(email_address=email_address)
                if user.email_address ==email_address:
                    return HttpResponseRedirect('/accounts/keep/')
                else:
                    pform.add_error(None, "unknown user, try again")
            except SignUp.DoesNotExist:
                pform.add_error(None, "this email doesn't exist in our system")
        else:
            pform = ResetForm()
    return render(request, 'reset.html', {'pform': pform})





