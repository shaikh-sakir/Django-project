from django.contrib import admin
from .models import Tweet

# Register your models here.
# after creating the new model we need to register it to the admin.py file 

admin.site.register(Tweet)