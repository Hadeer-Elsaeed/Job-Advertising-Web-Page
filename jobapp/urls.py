from django.urls import path
from jobapp import views

app_name = "jobapp"


urlpatterns = [
    path('', views.home_view, name='home'),
    path('jobs/',views.display_jobs,name='jobs'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-job/<int:id>/',views.apply_job, name='apply'),
    path('apply-job/<int:id>/save_applicant',views.save_applicant, name='save-applicant'),

]