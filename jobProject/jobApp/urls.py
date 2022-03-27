from django.urls import path
from jobApp import views

urlpatterns=[
path('',views.index),
path('Hyd/', views.HydJobsInfo),
path('Pune/', views.PuneJobsInfo),
path('Chennai/', views.ChennaiJobsInfo),
path('Mumbai/', views.MumbaiJobsInfo),
path('create/', views.add_view),
path('delete/<id>',views.delete_view),
path('update/<id>',views.update_view),
]
