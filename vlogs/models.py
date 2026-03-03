from django.db import models

class Home(models.Model):
    slide = models.ImageField(upload_to='photos/slide/')
    status = models.BooleanField(default=True)
    big_text = models.CharField(max_length=70, null=True, blank=True)
    small_text = models.CharField(max_length=120, null=True, blank=True) 


    
class Video_HomePage(models.Model):
    video = models.FileField(upload_to='videos/')  


class Management_Massage (models.Model):
    title = models.CharField(max_length=105)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Admin_images/')
    text = models.TextField(help_text="Write the CEO/Director Massage")
    others = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/blog_images/', null=True, blank=True)
    reference_link = models.URLField(max_length = 200, blank=True, null=True)  

    def __str__(self):
        return self.title 


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
        
class Local_Factory(models.Model):
    FACTORY_TYPE_CHOICES = [
        ('footwear', 'Footwear'),
        ('leather', 'leather'),
        ('tannery', 'Tannery'),
       
    ] 
    
    name = models.CharField(max_length=255)  
    type = models.CharField(max_length=20, choices=FACTORY_TYPE_CHOICES, null=True, blank=True)
    factory_address = models.CharField(max_length=1024, null=True, blank=True)  
    head_office_address = models.CharField(max_length=1024, null=True, blank=True)  
    website_address = models.CharField(max_length=200, null=True, blank=True)  
    managing_director = models.CharField(max_length=255, null=True, blank=True)
    business_contact_person = models.CharField(max_length=255, null=True, blank=True)
    product_line = models.CharField(max_length=1024, null=True, blank=True)  
    number_of_manpower = models.CharField(max_length=255, null=True, blank=True) 
    number_of_finishing_line = models.CharField(max_length=255, null=True, blank=True) 
    production_capacity = models.CharField(max_length=255, null=True, blank=True)
    social_certification = models.CharField(max_length=255, null=True, blank=True)
    export_country = models.CharField(max_length=255, null=True, blank=True)
    major_buyer = models.CharField(max_length=255, null=True, blank=True)
    production_area = models.CharField(max_length=1024, null=True, blank=True)  
    other_contact_person = models.CharField(max_length=255, null=True, blank=True)
    establishment_year = models.CharField(max_length=4, null=True, blank=True)  
    bond_license_status = models.CharField(max_length=100, null=True, blank=True)
    investment = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return self.name

    

class CompanyStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
        

class Partner(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.title
        
     
class CompanyProfile(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='company_profiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
        
