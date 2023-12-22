from rest_framework import serializers
from detection.models import UploadAlert

#create a class that will do the serialization
class UploadAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model=UploadAlert
        #fields that we will import from REST
        fields=('pk', 'image', 'user_ID', 'location', 'date_created', 'alert_receiver')
