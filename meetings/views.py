from meetings.models import UNMeetUser, Meeting
from meetings.serializers import MeetingSerializer, UNMeetUserSerializer
from rest_framework import generics


class UNMeetUserList(generics.ListCreateAPIView):
    queryset = UNMeetUser.objects.all()
    serializer_class = UNMeetUserSerializer


class UNMeetUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UNMeetUser.objects.all()
    serializer_class = UNMeetUserSerializer


class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class HostedMeetingsList(generics.ListAPIView):
    serializer_class = MeetingSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        host = self.kwargs['host']
        return self.model.objects.filter(host=host)

class AttendedMeetingsList(generics.ListAPIView):
    serializer_class = MeetingSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        attendant=self.kwargs['attendant']
        return Meeting.objects.filter(attendants__id__contains=attendant)