from django.contrib import admin
from django.urls import path
from . import views, job_views, cookie_views, job_orm_views, class_views, rest_views

urlpatterns = [
    path('index/', views.index),
    path('topics/', views.topics),
    path('countries/', views.countries),
    path('country/', views.country),
    path('country_info/', views.country_info),
    path('factorial/', views.factorial),
    path('listjobs/', job_views.list),
    path('addjob/', job_views.add),
    path('deletejob/<int:jobid>', job_views.delete_job),
    path('editjob/<int:jobid>', job_views.edit_job),
    path('updatejob/<int:jobid>', job_views.update_job),
    path('selectcity/', cookie_views.select_city),
    path('movies/', cookie_views.list_movies),
    path('langs/', views.session_names),
    path('ajaxdemo/', views.ajax_demo),
    path('datetime/', views.getdatetime),
    path('orm/listjobs/', job_orm_views.list_jobs),
    path('orm/addjob/', job_orm_views.add_job),
    path('orm/deletejob/<int:jobid>', job_orm_views.delete_job),
    path('orm/searchjobs/', job_orm_views.search_jobs),
    path('orm/getjobs/', job_orm_views.get_jobs),
    path('about/', class_views.AboutView.as_view()),
    path('jobs/', class_views.JobsListView.as_view()),
    path('restjobs/', rest_views.job_process),
    path('restjobs/<int:id>', rest_views.one_job_process),
    path('restclient/', rest_views.job_client),

]
