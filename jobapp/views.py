from django.shortcuts import render
from jobapp.forms import *
from jobapp.models import *
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage




# Create your views here.
def home_view(request):   
    return render(request, 'jobapp/index.html')

    
def display_jobs(request):
    job_list = Job.objects.order_by('id')
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

        'page_obj': page_obj,

    }
    return render(request, 'jobapp/job-list.html', context)


def single_job_view(request,id):
    """
    Provide the ability to view job details
    """
    job = get_object_or_404(Job, id=id)
    page_number = request.GET.get('page')

    context = {
        'job': job,

    }
    return render(request, 'jobapp/job-single.html', context)


def apply_job(request,id):
    employee_form = EmployeeForm()
    return render(request,'jobapp/apply_job.html',{'employee_form':employee_form})


def save_applicant(request , id):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            new_employee = form.save(commit=False)
            # new_employee = Employee(docfile = request.FILES['docfile'])
            new_employee.id = request.POST['id']
            new_employee.first_name = request.POST['first_name']
            new_employee.last_name = request.POST['last_name']
            new_employee.email = request.POST['email']

            filename = request.FILES['cv']
            fs = FileSystemStorage()
            filename = fs.save(filename.name, filename)

            file_ext = filename[-4:]
            if file_ext == '.doc' or file_ext == '.pdf':  
                new_employee.save()

        
        else:
            return HttpResponse(form.errors)
    else:
        return render(request,'jobapp/applied.html')