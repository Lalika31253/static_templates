from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    ctx = {
        "theme": "cupcake",
        "name": "ComIT",
        "students": 10,
        "names": ["Bob", "Sarah", "Don", "Inna", "Alex", "Tim", "Greg", "Anna", "Ryan", "Sam"],
        "is_active": True
    }
    return render(request, 'home.html', ctx)

@login_required(login_url='login')
def contact(request):
  ctx = {
     "theme": "retro",
     "medias": ["Facebook", "LinkedIn", "Instagram", "Telegram"]
  }
  return render(request, 'contact.html', ctx)

@login_required(login_url='login')
def about(request):
    ctx = {
        "theme": "valentine"
    }
    return render(request, 'about.html', ctx)

@login_required(login_url='login')
def news(request):
    ctx = {
        "theme": "caramellatte",
        "news": ["February", "March", "April"]
    }
    return render(request, 'news.html', ctx)