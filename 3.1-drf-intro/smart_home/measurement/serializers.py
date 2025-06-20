from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    # Для списка датчиков (GET /sensors/)
     # Для создания датчика (POST /sensors/)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    # read_only=True - поле только для чтения (не требует ввода при создании/обновлении)
    # many=True - указывает, что это отношение "один-ко-многим" (у датчика много измерений)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']