from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)  
    description = models.CharField(max_length=300, blank=True, null= True)  
    company = models.CharField(max_length=100, blank=True, null= True)
    deadline = models.DateField( blank=True, null= True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    skills_required = models.CharField(max_length=100, blank=True, null=True)    
    salary = models.CharField(max_length=100, blank=True, null=True)  
    duration = models.CharField(max_length=100, blank=True, null=True)
    others_facility = models.TextField(blank=True, null=True)
    circular = models.FileField(upload_to='job_circulars/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Resume(models.Model):
    job = models.ForeignKey(Job, related_name='resumes', on_delete=models.CASCADE)

    # Existing File (CV)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateField(auto_now_add=True)

    # Basic Info
    name = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    expected_salary = models.CharField(max_length=50, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    # Passport Info
    passport_number = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    passport_expire_date = models.DateField(blank=True, null=True)

    # Category
    category = models.CharField(max_length=100, blank=True, null=True)

    # Apply Type
    APPLY_TYPE_CHOICES = (
        ('self', 'Self Apply'),
        ('agent', 'Agent Apply'),
    )
    apply_type = models.CharField(
        max_length=10,
        choices=APPLY_TYPE_CHOICES,
        blank=True,
        null=True
    )

    # Additional Documents (Passport Copy etc.)
    passport_copy = models.FileField(upload_to='passport_copies/', blank=True, null=True)

    def __str__(self):
        return f"{self.job.title} --- {self.name} --- Experience: {self.experience} Years --- Apply Date: {self.submitted_at}"
        
       
       
       












class Student(models.Model):
    name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=100, unique=True)
    batch = models.CharField(max_length=50)
    final_cgpa = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.reg_no} - {self.name}"


class SemesterResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="semesters")
    semester = models.IntegerField()
    sgpa = models.FloatField(null=True, blank=True)
    average_grade = models.CharField(max_length=10, null=True, blank=True)
    cgpa = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'semester')

    

class PermanentResult(models.Model):

    batch = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=100)
    semester = models.IntegerField()
    sgpa = models.FloatField(null=True, blank=True)
    average_grade = models.CharField(max_length=10, null=True, blank=True)
    cgpa = models.FloatField(null=True, blank=True)
    final_cgpa = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reg_no', 'semester')

    def __str__(self):
        return f"{self.reg_no} - Semester {self.semester}"
    
    