from django.contrib import admin

# Register your models here.
from .models import User,Blog,QuerySend


#add Models field to admin pannel
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(QuerySend)