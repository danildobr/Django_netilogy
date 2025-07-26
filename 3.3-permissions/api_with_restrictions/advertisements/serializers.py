from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        if self.context['request'].method == 'POST' or 'status' in data:
            user = self.context['request'].user
            
            open_ads = 0
            if data.get('status', AdvertisementStatusChoices.OPEN) == AdvertisementStatusChoices.OPEN:
                open_ads = Advertisement.objects.filter(
                    creator=user, 
                    status=AdvertisementStatusChoices.OPEN
                ).count()
                if open_ads >= 10:
                    raise serializers.ValidationError(
                        "Нельзя иметь более 10 открытых объявлений"
                    )
        return data