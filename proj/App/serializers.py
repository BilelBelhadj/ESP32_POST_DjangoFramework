#serializers du rest API pour l affichage des donnees 

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from App.models import Obj


class objSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Obj
        fields = ['nameMicro', 'nameCapteur', 'donnee']



        