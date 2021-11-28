from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from meetings import views

urlpatterns = [
    path('UNMeetUser/', views.UNMeetUserList.as_view()),
    path('UNMeetUser/<int:pk>/', views.UNMeetUserDetail.as_view()),
    path('meetings/', views.MeetingList.as_view()),
    path('meetings/<str:pk>/', views.MeetingDetail.as_view()),
    path('hostedmeetings/<int:host>/', views.HostedMeetingsList.as_view()),
    path('attendedmeetings/<int:attendant>/', views.AttendedMeetingsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)