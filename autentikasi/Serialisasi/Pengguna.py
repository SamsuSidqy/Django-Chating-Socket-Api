from rest_framework import serializers
from base.models import Pengguna
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.fields import CharField

class PenggunaSerilisasi(serializers.ModelSerializer):   
    class Meta:
        model = Pengguna
        fields = ('username','password','created_at','email','id')

    def create(self,validated_data):
        pswd = validated_data.get('password')
        print(pswd)
        hasing = make_password(pswd)
        validated_data['password'] = hasing
        return super().create(validated_data)

