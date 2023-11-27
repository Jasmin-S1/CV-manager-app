from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='user_register'),
    path('login/', views.loginUser, name='user_login'),
    path('logout/', views.logoutUser, name='user_logout'),
    path('applications/', views.showJobs, name='all_jobs'),
    path('delete-job/<str:pk>/', views.deleteJob, name='delete_job'),
    path('add_job/', views.addJob , name='add_job'),
    path('job_search/', views.searchJob, name='job_search'),
    path('toggle_feedback/<int:job_id>', views.toggleFeedback, name='toggle_feedback')
]   