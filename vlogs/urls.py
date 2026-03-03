from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.logo_animation, name="logo"),
    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('about/choose/', views.choose, name='choose'),
    path('about/missionvision/', views.missionvision, name='missionvision'),
    path('about/management_massage/', views.management_massage, name='management_massage'),

    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog_details'),
    path('contact/', views.contact_view, name='contact'), 
    path('about/company-profile/', views.company_profile, name='company_profile'),
    path('about/who-we-are/', views.who_we_are, name='who_we_are'),
    path('industries/', views.industries_view, name='industries'),
    path('parthner/', views.parthner, name='parthner'),
    
    path('local/option', views.option ,name='local'),
    path('local/footwear', views.footwear ,name='footwear'),
    path('local/leather', views.leather ,name='leather'),
    path('local/tannery', views.tannery ,name='tannery'),  

] 



