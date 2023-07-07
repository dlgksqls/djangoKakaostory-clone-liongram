from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import decore
from .models import Contents,Comment
from .forms import ContentBaseForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    contents_list = Contents.objects.all().order_by('-created_at')
    context = {
        'contents' : contents_list
    }
    return render(request,'home.html',context)

def created_view(request): 
    if request.method == 'GET':
        return render(request,'story/create.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        title = request.POST.get('title')
        Contents.objects.create(
            title = title,
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('story:home')
    
def detail_view(request,id):
    try:
        content = Contents.objects.get(id=id)
    except Contents.DoesNotExist:
        return redirect('index')
    context = {
        'content':content,
        'form':ContentBaseForm(),
    }
    return render(request,'story/detail.html',context)

def delete_view(request,id):
    content = get_object_or_404(Contents,id=id)
    if request.method == 'GET':
        context = {
            'content' : content
        }
        return render(request,'story/delete.html',context)
    else:
        content.delete()
        return redirect('story:home')
    
def update_view(request,id):
    content = get_object_or_404(Contents,id=id)
    if request.method == 'GET':
        context = {
            'content':content
        }
        return render(request,'story/create.html',context)
    elif request.method == 'POST':
            new_image = request.FILES.get('image')
            new_content = request.POST.get('content')
            
            if new_image:
                content.image.delete()
                content.image = new_image
            content.content = new_content
            content.save()
            return redirect('story:home',content,id)
    
def user(request,id):
    return render(request,'index.html')