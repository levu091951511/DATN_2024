from rest_framework import serializers
from .models import Account, Nguongcanhbao, Factlichsugia, Factchibao

from django.contrib.auth.hashers import make_password, check_password



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class NguongcanhbaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nguongcanhbao
        fields = '__all__'

class FactlichsugiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factlichsugia
        fields = '__all__'

class FactchibaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factchibao
        fields = '__all__'


