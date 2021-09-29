from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^employee/(?P<id>[0-9]+)/$', views.EmployeeView.as_view()),
    url(r'^employee/$', views.EmployeeListView.as_view()),

    url(r'^degree/(?P<id>[0-9]+)/$', views.DegreeView.as_view()),
    url(r'^degree/$', views.DegreeListView.as_view()),

    url(r'^subject/(?P<id>[0-9]+)/$', views.SubjectView.as_view()),
    url(r'^subject/$', views.SubjectListView.as_view()),

    url(r'^schedule_interview/(?P<id>[0-9]+)/$', views.InterviewScheduleView.as_view()),
    url(r'^schedule_interview/$', views.InterviewScheduleListView.as_view()),

    url(r'^document/(?P<id>[0-9]+)/$', views.DocumentView.as_view()),
    url(r'^document/$', views.DocumentListView.as_view()),

    url(r'^account_setup/(?P<id>[0-9]+)/$', views.AccountSetupView.as_view()),
    url(r'^account_setup/$', views.AccountSetupListView.as_view()),

    url(r'^project_allocation/(?P<id>[0-9]+)/$', views.ProjectAllocationView.as_view()),
    url(r'^project_allocation/$', views.ProjectAllocationListView.as_view()),

    url(r'^leave_management/(?P<id>[0-9]+)/$', views.LeaveManagementView.as_view()),
    url(r'^leave_management/$', views.LeaveManagementListView.as_view()),

    url(r'^salary_account/(?P<id>[0-9]+)/$', views.SalaryAccountView.as_view()),
    url(r'^salary_account/$', views.SalaryAccountListView.as_view()),

    url(r'^attendance/(?P<id>[0-9]+)/$', views.AttendanceView.as_view()),
    url(r'^attendance/$', views.AttendanceListView.as_view()),

    url(r'^experiance_letter/(?P<id>[0-9]+)/$', views.ExperianceLetterView.as_view()),
    url(r'^experiance_letter/$', views.ExperianceLetterListView.as_view()),

]