from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'chat/index.html', {})

def room(request):
  return render(request, 'chat/chatroom.html', {})