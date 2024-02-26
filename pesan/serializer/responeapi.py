from rest_framework import serializers
from base.models import Pengguna,Messages


class ContactUser(serializers.ModelSerializer):
	class Meta:
		model = Pengguna
		fields = ('username','id')

class MessageUser(serializers.ModelSerializer):
	class Meta:
		model = Messages
		fields = '__all__'
