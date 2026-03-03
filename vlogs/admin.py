from django.contrib import admin
from . models import *

class BlogAdmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Video_HomePage)
admin.site.register(Management_Massage)
admin.site.register(Local_Factory)
admin.site.register(Partner)
from .models import CompanyStat

@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "suffix")
    

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    