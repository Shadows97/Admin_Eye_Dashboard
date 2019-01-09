from rest_framework import serializers

from Dashboard.models import *


class Disk_Info_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disk_info
        fields = ('total','used','free')