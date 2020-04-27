from django.shortcuts import render
from smc_app.models import ChatData

# Create your views here.
def index(request):
    return render(request,'smc_app/index.html')

def majju(request):
    # chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    # chatdata_dict = {'chatdata':chatdata}

    if request.method == 'POST':
        textdata = request.POST.get("Textinput")
        chattext = ChatData(name='M',text=textdata)
        if len(textdata) > 0:
            chattext.save()
        # print('data saved in chat database for majju')

    else:
        print('Error saving data')

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata}
    return render(request,'smc_app/majju.html',context=chatdata_dict)



def sallu(request):
    # chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    # chatdata_dict = {'chatdata':chatdata}

    if request.method == 'POST':
        textdata = request.POST.get("Textinput")
        chattext = ChatData(name='S',text=textdata)
        if len(textdata) > 0:
            chattext.save()
        # print('data saved in chat database for majju')

    else:
        pass

    chatdata = ChatData.objects.order_by('-sentat')[:100][::-1]
    chatdata_dict = {'chatdata':chatdata}
    return render(request,'smc_app/sallu.html',context=chatdata_dict)
