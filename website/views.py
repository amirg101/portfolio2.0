from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages


from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    projects=Project.objects.all()
    info=Info.objects.first()
    
    skills=Skills.objects.all()
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            form.save()
            messages.info(request, 'Thank you..... Your message has been sent successfully!!')
            # return HttpResponse('Thanks for contacting us!')
            return redirect('/#contact')
    else:
        form = contactForm()

    return render(request,'index.html',{"projects":projects,"form":form,"info":info,"skills":skills})


def allprojects(request):
    project1=Project.objects.all()

    
    return render(request,'projects.html',{"projects":project1})

def test(request):
    return render(request,'test.html')

def details(request,pk):
    try:
        proj=Project.objects.get(id=pk)
        pros=proj.imageproject_set.all()

    except:
        proj=[]
        pros=[]
    return render(request,'details.html',{"project":proj,"pros":pros})