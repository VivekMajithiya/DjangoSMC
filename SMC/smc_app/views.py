from django.shortcuts import render
from smc_app.models import ChatData
from smc_app.forms import UserForm, UserProfileInfoForm
from smc_app.models import UserProfileInfo


#Below imports for login page form and validations
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'smc_app/index.html')

def register(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
             print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'smc_app/registration.html',
                                        {'user_form':user_form,
                                        'profile_form':profile_form,
                                        'registered':registered})

@login_required
def majju(request):
    if request.method == 'POST':
        textdata = request.POST.get("Textinput")
        chattext = ChatData(name='M',text=textdata)
        if len(textdata) > 0:
            chattext.save()
    else:
        pass

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata}
    return render(request,'smc_app/majju.html',context=chatdata_dict)


@login_required
def sallu(request):
    if request.method == 'POST':
        textdata = request.POST.get("Textinput")
        chattext = ChatData(name='S',text=textdata)
        if len(textdata) > 0:
            chattext.save()
    else:
        pass

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata}
    return render(request,'smc_app/sallu.html',context=chatdata_dict)

def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username') # this is the name in the html element on the forms
        password = request.POST.get('InputPassword1') #this is the password field name atribute in forms

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                if username == 'M':
                    return HttpResponseRedirect(reverse('smc_app:majju'))
                else:
                    return HttpResponseRedirect(reverse('smc_app:sallu'))
            else:
                return render(request,'smc_app/login.html',{'loginmesssage':'User not active contact admin!!'})
        else:
            print("Someone logged in and login failed")
            return render(request,'smc_app/login.html',{'loginmesssage':'Invalid login id or password!!'})

    else:
        return render(request,'smc_app/login.html',{'loginmesssage':''})

@login_required
def userlogout(request):
    logout(request)
    return render(request,'smc_app/login.html',{'loginmesssage':'You are logged out, thank you for using SMC!!'})
