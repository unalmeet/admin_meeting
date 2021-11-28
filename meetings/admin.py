from django.contrib import admin
from meetings.models import Meeting, UNMeetUser

admin.site.register(UNMeetUser)
admin.site.register(Meeting)