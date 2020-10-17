from django.urls import path
from . import views
from . import HodViews


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.ShowLoginPage, name='ShowLoginPage'),
    path('doLogin', views.doLogin, name='DoLogin'),
    path('Logout_user/', views.Logout_user, name='Logout_user'),
    path('get_user_details/', views.GetUserDetails, name='GetUserDetails'),
    path('admin_home/', HodViews.admin_home, name='admin_home'),
    path('add_staff/', HodViews.add_staff, name='add_staff'),
    path('add_staff/', HodViews.add_staff, name='add_staff'),
    path('add_staff_save/', HodViews.add_staff_save, name='add_staff_save'),
    path('add_course/', HodViews.add_course, name='add_course'),
    path('add_course_save/', HodViews.add_course_save, name='add_course_save'),
    path('add_student/', HodViews.add_student, name='add_student'),
    path('add_student_save/', HodViews.add_student_save, name='add_student_save'),
    path('add_subjects/', HodViews.add_subjects, name='add_subjects'),
    path('add_subjects_save/', HodViews.add_subjects_save, name='add_subjects_save'),
    path('manage_staff/', HodViews.manage_staff, name='manage_staff'),
    path('manage_student/', HodViews.manage_student, name='manage_student'),
    path('manage_course/', HodViews.manage_course, name='manage_course'),
    path('manage_subject/', HodViews.manage_subject, name='manage_subject'),

]