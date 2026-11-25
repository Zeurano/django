from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseNotFound, JsonResponse


from django.http import HttpResponse
NAV_LINKS = '<br> Follow this link to continue: <a href="/about/">about</a> | <a href="/index1/">index</a> | <a href="/name/">name</a>'

# Create your views here.
def index1(request):
    return HttpResponse(f"<h2>HELLO EGOIST !</h2> {NAV_LINKS}")

def about(request):
    return HttpResponse(f"BLUE LOCK PROJECT STARTED. {NAV_LINKS}")

def name(request,name=""):
    return HttpResponse(f"My name is ISAGI YOICHI, and I am THE BEST in the WORLD! {name} {NAV_LINKS}")

def home(request):
    method=request.method
    path=request.path
    user_agent=request.headers.get("User-Agent")
    host=request.get_host()
    all=f"<p>Method: {method}</p><p>path: {path}</p><p>user agent: {user_agent}</p><p> host: {host}</p> "
    return HttpResponse(all)

def user(request,username):
    return HttpResponse(f"profile name: {username}")

def news(request,id ):
    return HttpResponse(f"global new №{id} ")
def newsbluelock(request,id ):
    return HttpResponse(f"blue lock new №{id} ")
def newsneoego(request,id ):
    return HttpResponse(f"neo egoist project new №{id} ")

def personality(request):
    age=request.GET.get('age', 'UNKNOWN')
    location=request.GET.get('location', 'UNKNOWN')
    return HttpResponse(f"Age: {age}, Location: {location}")



def fake(request):
    return redirect('/index1/')
def NotFound(request):
    return HttpResponseNotFound("<h1>404 Page Not Found</h1>")
def json(request):
    data={'Isagi':'Yoichi','password': 123}
    return JsonResponse(data)
def set_cookie(request):
    response=HttpResponse('successfuly downloaded cookie')
    response.set_cookie('user_id','12345', max_age=3600)
    return response
def get_cookie(request):
    user_id=request.COOKIES.get('user_id', 'unknown')
    return HttpResponse(f'your id:{user_id}')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/view_task.html', {'task': task})


def create_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'tasks/create_task.html')


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'tasks/edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('index')
    return render(request, 'tasks/delete_task.html', {'task': task})

from .forms import GiveForm
def give(request):
    if request.method=="POST":
        form=GiveForm(request.POST, request.FILES)
        if form.is_valid():
            namefv=request.POST.get('namef')
            agefv=request.POST.get('agef')
            emailfv=request.POST.get('emailf')
            datefv=request.POST.get('datef')
            filefv=request.POST.get('filef')
            passwordfv=request.POST.get('passwordf')
            return HttpResponse(f'your name: {namefv} \n you are:{agefv} years old \n your email is: {emailfv} \n today`s day is: {datefv} \n your file is here: {filefv}, your password is {passwordfv} ')
    else:
        form= GiveForm()
    return render (request,'tasks/give.html', {'form':form})
