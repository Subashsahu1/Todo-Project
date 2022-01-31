from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from app.forms import NoteForm
from.models import Note
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = NoteForm()
        Notes = Note.objects.filter(user=user).order_by('priority')# Use .order_by('-priority) to reverse the order
        return render(request,'index.html',context={'form':form,'notes':Notes})

def login(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')

        else:
            context = {"form" : form }
            return render(request,'login.html',context)

    else:
        form = AuthenticationForm()
        context = {
        "form" : form
        }
        return render(request,'login.html',context)

def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        context = {
        "form" : form
        }

        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',context)

    else:
        form = UserCreationForm()
        context = {
        "form" : form
        }
        return render(request,'signup.html',context)

@login_required(login_url='login')
def AddNote(request):
    if request.user.is_authenticated:
        user = request.user
        form = NoteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Note = form.save(commit=False)
            Note.user = user
            Note.save()
            return redirect("home")
        else:
            return render(request,'index.html',context={'form':form})


def deleteTodo(request,id):
    Note.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request,id, status):
    todo = Note.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login')