from django.contrib import admin
from . models import *

class companyadmin(admin.ModelAdmin): 
     list_display = ['company_name']    
     prepopulated_fields = {'slug' : ('company_name',)}
     
class newsarticleadmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 

class eventadmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 

class Leadersadmin(admin.ModelAdmin): 
     list_display = ['name']    
     prepopulated_fields = {'slug' : ('name',)}

     
admin.site.register(Company, companyadmin)
admin.site.register(NewsArticle, newsarticleadmin)
admin.site.register(Leaders, Leadersadmin) 
admin.site.register(Factory) 
admin.site.register(type) 
admin.site.register(Event, eventadmin) 
admin.site.register(Gallery) 
admin.site.register(Image) 
admin.site.register(Video) 


admin.site.site_header = "JSBD Limited Admin"
admin.site.site_title = "JSBD Limited Admin Panel"
admin.site.index_title = "Contact: +8801626902404"