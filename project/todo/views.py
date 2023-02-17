from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    items = Todo.objects.all()

    if request.method == 'POST':
        form  = TodoForm(request.POST)
        form.save()

    form = TodoForm()
    return render(request, 'todo/index.html',{'form':form,'items':items})

def delete(request, id):
    pos=Todo.objects.get(pk=id)
    pos.delete()
    
    
    return redirect('/')