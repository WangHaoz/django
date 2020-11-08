from rest_framework import serializers

from App.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('url', 'id',  'g_name', 'g_price')