import emoji
from django.shortcuts import render
from smc_app.models import ChatData
from smc_app.forms import UserForm, UserProfileInfoForm
from smc_app.models import UserProfileInfo
from django.core.mail import send_mail
from smc_app.gatepass import Gatepass
from datetime import datetime
from django.core.files.storage import FileSystemStorage

#Below imports for login page form and validations
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'smc_app/index.html')

def notify(request):
    if request.method == 'POST':
        try:
            gatepass=Gatepass()
            mail_data=(gatepass.get_mail_data(gatepass.get_key())).decode().split(":")
            send_mail(mail_data[0]+datetime.now().strftime("%d/%m/%Y %H:%M:%S"),mail_data[1],mail_data[2],[mail_data[3]],auth_password=mail_data[4])
            chatmessage="Notification sent"
        except:
            chatmessage="Error in sending notification check with admin!!"
        finally:
            chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
            chatdata_dict = {'chatdata':chatdata,'chatmessage':chatmessage}
            return render(request,'smc_app/sallu.html',context=chatdata_dict)

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
    files_allowed=['jpg','jpeg','png','gif']
    chatmessage=''
    if request.method == 'POST':
        textdata = emoji.emojize(request.POST.get("Textinput"))
        if request.FILES:
            uploaded_file = request.FILES['uploadedfile']
            if uploaded_file.name.split('.')[-1] in files_allowed:
                textdata=uploaded_file.name
                fs=FileSystemStorage()
                fs.save(uploaded_file.name,uploaded_file)
                chattext = ChatData(name='M',text=textdata,ctype='I')
            else:
                chatmessage = "Only images can be uploaded!!"
        else:
            chattext = ChatData(name='M',text=textdata)

        if len(textdata) > 0:
            chattext.save()
    else:
        pass

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata,'chatmessage':chatmessage}
    return render(request,'smc_app/majju.html',context=chatdata_dict)


@login_required
def sallu(request):
    files_allowed=['jpg','jpeg','png','gif']
    chatmessage=''
    if request.method == 'POST':
        textdata = emoji.emojize(request.POST.get("Textinput"))
        if request.FILES:
            uploaded_file = request.FILES['uploadedfile']
            if uploaded_file.name.split('.')[-1] in files_allowed:
                textdata=uploaded_file.name
                fs=FileSystemStorage()
                fs.save(uploaded_file.name,uploaded_file)
                chattext = ChatData(name='S',text=textdata,ctype='I')
            else:
                chatmessage = "Only images can be uploaded!!"
        else:
            chattext = ChatData(name='S',text=textdata)

        if len(textdata) > 0:
            chattext.save()
    else:
        pass

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata,'chatmessage':chatmessage}
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
                    try:
                        gatepass=Gatepass()
                        mail_data=(gatepass.get_mail_data(gatepass.get_key())).decode().split(":")
                        send_mail(mail_data[0]+datetime.now().strftime("%d/%m/%Y %H:%M:%S"),mail_data[1],mail_data[2],[mail_data[3]],auth_password=mail_data[4])
                    except:
                        print("error sending email")
                    finally:
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
