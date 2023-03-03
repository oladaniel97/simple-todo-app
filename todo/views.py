from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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