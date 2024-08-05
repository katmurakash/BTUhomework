
from django.shortcuts import render
from .models import Book, User

def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html')

def profile(request, pk):
    print(pk)
    user = User.objects.get(id=pk)
    books = user.books.all()
    context = {"books": books}
    return render(request, 'base/profile.html', context)
