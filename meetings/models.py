from hashid_field import HashidAutoField
from django.db import models
from django.utils import timezone

class UNMeetUser (models.Model):
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return 'UNMeetUser ' + str(self.id)

class Meeting(models.Model):
    link = HashidAutoField(primary_key=True,prefix="UNMEET",min_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()
    host = models.ForeignKey(UNMeetUser,related_name="host_meeting", on_delete= models.CASCADE)
    attendants = models.ManyToManyField(UNMeetUser, related_name="attendants_meeting")

    def __str__(self):
        return self.name
    


# class MeetingAttendants(models.Model):
#     unmeetuser = models.ForeignKey(UNMeetUser, on_delete=models.CASCADE)
#     meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
#     date_invited = models.DateTimeField(auto_now=True)