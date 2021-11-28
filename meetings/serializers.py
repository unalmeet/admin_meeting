from django.core import validators
from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.utils import model_meta
from rest_framework.validators import UniqueValidator
from meetings.models import Meeting, UNMeetUser

class UNMeetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UNMeetUser
        fields = ["id"]


class MeetingSerializer(serializers.ModelSerializer):
     
    link = HashidSerializerCharField(
        source_field="meetings.Meeting.link", read_only=True
    )
    class Meta:

        model = Meeting
        fields = [
            "link",
            "name",
            "description",
            "date_created",
            "date_start",
            "date_end",
            "host",
            "attendants"
        ]
        read_only_fields = ['date_created']


    def update(self, instance, validated_data):
         if(getattr(instance,'host') == validated_data.get('host')):
             serializers.raise_errors_on_nested_writes('update', self, validated_data)
             info = model_meta.get_field_info(instance)
             m2m_fields = []
             for attr, value in validated_data.items():
                 if attr in info.relations and info.relations[attr].to_many:
                     m2m_fields.append((attr, value))
                 else:
                     setattr(instance, attr, value)

             instance.save()

             for attr, value in m2m_fields:
                 field = getattr(instance, attr)
                 field.set(value)

             return instance
         else:
             raise ValidationError('No es posible cambiar el host de la reunion')