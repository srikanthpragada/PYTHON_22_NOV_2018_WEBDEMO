from django.contrib import admin
from django.urls import path
from . import views, job_views, cookie_views, job_orm_views

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
    path('orm/listjobs/', job_orm_views.list),
    path('orm/addjob/', job_orm_views.add),
    path('orm/deletejob/<int:jobid>', job_orm_views.delete_job),
    path('orm/searchjobs/', job_orm_views.search_jobs),
    path('orm/getjobs/', job_orm_views.get_jobs),

]
