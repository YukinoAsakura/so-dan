from django.shortcuts import render,HttpResponse,redirect 
from .models import UniversityEmail,University,Profile,Quest,Chat,Article
from django.utils import timezone
from django.http import Http404

# Create your views here.
def top(request):
    return render(request, 'albite/top.html')

def login(request):
    if request.method == 'POST':
        profile = Profile.objects.create(name=request.POST['name'],email=request.POST['email'],password=request.POST['pass'])
        profile.save()
        context={
            "profile":profile,
        }
        return redirect("top")
    return render(request, 'albite/join.html')

def quest(request):
    if request.method == 'POST':
        article = Article.objects.create(title=request.POST['title'],body=request.POST['text'])
        article.save()
        context={
            "article":article,
        }
        return redirect("top")
    return render(request,'albite/question.html')

def index(request):
    context ={
        "articles":Article.objects.all()
    }
    #article = Article(titel=request.POST['title'],body=request.POST['text'])
        
    return render(request,'albite/top.html',context)

def hello(request):
    date = {
        'name':'Alice',
        'weather':'CLOWDY',
        'weather_detail':['Temperture: 23℃','Humidity:40%','Wind:5m/s'],
        'isGreatForture':True,
        'forture':'Great Fortune!'
    }
    return render(request, 'albite/hello.html',date)

def redirect_test(request):
    return redirect(hello)

def detail(request,article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Quest does not exist")

    if request.method == 'POST':
        chats = Chat(quest=article,text = request.POST.get('ans'))
        chats.save()
    context={ 'article':article,
               'chats':article.chats.order_by('-time') }
    return render(request, 'albite/detail.html',context)

def update(request, article_id):
    try:
        artile = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    context={
        "article_id": article_id}
    return render(request, 'albite/tbd.html',context)

def delete(request, article_id):
    return redirect(index)

def mypage(request):
    return render(request, 'albite/mypage.html')