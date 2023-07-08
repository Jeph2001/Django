from django.shortcuts import render
from .forms import SignupForm, LoginForm
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





