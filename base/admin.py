from django.contrib import admin

# Register your models here.
from .models import Book, Author, User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)


