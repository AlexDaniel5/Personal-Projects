from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # Even though we didn't define id, there is automatically an id field in the model
        fields = ('id', 'code', 'host', 'guestCanPause', 'voteToSkip', 'createdAt')