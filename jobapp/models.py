from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator


# Create your models here.
JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    # GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    # gender = models.CharField(choices=GENDER_CHOICES, max_length = 128)
    # mobile = models.CharField(unique=True, max_length = 11, validators=[RegexValidator(regex='^\w{11}$', message='Mobile number should be strictly of 11 digits.')])
    cv = models.FileField(upload_to="uploads/", validators=[FileExtensionValidator(allowed_extensions=['pdf','docs'])])
    def __str__(self):
        return self.first_name
    
    
class Job(models.Model):
    title = models.CharField(max_length = 150) 
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    salary = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length = 300)
    company_name = models.CharField(max_length=300)
    img = models.ImageField(default="",upload_to='images/')
    last_date = models.DateField()
    # employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    
class Applicant(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

