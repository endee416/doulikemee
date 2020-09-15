from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import destinations, credentials4
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.

def actualhome(request):
    return render(request, 'actualhome.html')

part1 = destinations()
part1.name='gender'
part1.question = "What is Dee's favorite color"
part1.option1 = "red"
part1.option2 = 'blue'
part1.option3 = 'black'
part1.option4 = 'white'


part2=destinations()
part2.name='gender2'
part2.question = "What is Dee's social life like"
part2.option1 = 'introvert'
part2.option2 = 'extrovert'
part2.option3 = 'ambivert'
part2.option4 = 'just sad'


part3 = destinations()
part3.name='gender3'
part3.question = "What is Dee's age"
part3.option1 = '19'
part3.option2 = '20'
part3.option3 = '21'
part3.option4 = '22'


part4 = destinations()
part4.name='gender4'
part4.question = "What is Dee's sexuality"
part4.option1 = 'straight'
part4.option2 = 'gay'
part4.option3 = 'bisexual'
part4.option4 = 'asexual'

names=['gender1','gender2','gender3','gender4']



allparts=[part1, part2, part3, part4]

def home(request):
    if request.method=='POST':
         global question1
         question1=request.POST.get('gender')
         global question2
         question2=request.POST.get('gender2')
         global question3
         question3=request.POST.get('gender3')
         global question4
         question4=request.POST.get('gender4')
         return redirect('secondpage')


    else:
        return render(request, "home.html", {'parts': allparts})

def secondpage(request):
    if request.method=='POST':
        global question5
        question5=request.POST['deename']
        global question6
        question6=(request.POST.get('day'), request.POST.get('month'))
        global question7
        question7=request.POST['rstatus']
        global question8
        question8=request.POST['dept']
        global question9
        question9=request.POST['fmeal']
        global question10
        question10=request.POST['siblings']
        global question11
        question11=request.POST['tvshow']
        global question12
        question12=request.POST['hometown']
        global question13
        question13=request.POST['priedu']
        global question14
        question14=request.POST['secedu']
        return redirect('thirdpage')
    else:
        return render(request, 'secondpage.html')

def thirdpage(request):
    if request.method=='POST':
        global question15
        question15=request.POST['sports']
        global question16
        question16=(request.POST.get('hobby1'), request.POST.get('hobby2'), request.POST.get('hobby3'))
        global question17
        question17=request.POST['church']
        global question18
        question18=request.POST['anime']
        global question19
        question19=request.POST['favanime']
        global question20
        question20=request.POST.getlist('personality')
        global question21
        question21=(request.POST.get('personalitytrait1'), request.POST.get('personalitytrait2'), request.POST.get('personalitytrait3'))
        return redirect('fourthpage')
    else:
        return render(request, 'thirdpage.html')

def fourthpage(request):
    if request.method=='POST' and request.FILES['clientimage']:
        clientimage=request.FILES['clientimage']
        question22=request.POST.get('clientname')
        p=credentials4.objects.create(favcolor=question1, sociallife=question2, age=question3, sexuality=question4, fullname=question5, birthday=question6, rstatus=question7,dept=question8,favmeal=question9, siblings=question10, tvshow=question11, hometown=question12, priedu=question13, secedu=question14, sports=question15, hobby=question16, church=question17,anime=question18, favanime=question19, personality=question20, otherpersonality=question21, clientname=question22, imagetogether=clientimage)
        p.save()
        return redirect('fifthpage')
    else:
        return render(request, 'fourthpage.html')

def fifthpage(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('actualhome')

    
    else:

        return render(request, 'fifthpage.html')




def login(request):
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('hello')
        else:
            messages.info(request, 'You are an idiot!! go and create an account or enter the correct credentials!')
            return redirect('login')


    else:
        return render(request, 'login.html')

def report(request):
    
    if request.method=='POST':
        return redirect('fourthpage')
    else:
        return render(request, 'report.html')

def hello(request):
    return render(request, 'helo.html')

    









