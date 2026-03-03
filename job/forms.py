# from django import forms
# from .models import Resume

# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = ['resume']


# from django import forms
# from .models import Resume

# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = ['resume', 'name', 'experience', 'position', 'contact', 'email', 'expected_salary', 'remark']

from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'resume', 'passport_copy',  # files
            'name', 'experience', 'position', 'contact', 'email', 'expected_salary', 'remark',
            'address', 'passport_number', 'date_of_birth', 'category',
            'passport_issue_date', 'passport_expire_date', 'apply_type'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'passport_issue_date': forms.DateInput(attrs={'type': 'date'}),
            'passport_expire_date': forms.DateInput(attrs={'type': 'date'}),
            'apply_type': forms.Select(choices=[('self', 'Self Apply'), ('agent', 'Agent Apply')])
        }
        
        