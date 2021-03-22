from django import forms
from jobapp.models import *
from django.core.validators import RegexValidator


class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['last_date'].label = "Submission Deadline :"
        self.fields['img'].label = "Company Image:"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Bangladesh',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$800 - $1200',
            }
        )                
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
                
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )           



    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "salary",
            "description",
            "company_name",
            "img",
            "last_date",
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type


    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        return job
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = ('first_name','last_name','email','cv')
        

