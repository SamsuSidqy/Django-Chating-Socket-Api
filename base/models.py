from django.db import models
from django.contrib.auth.models import AbstractUser


class Pengguna(AbstractUser):
	username = models.CharField(max_length=200,unique=True)
	password = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	

class Messages(models.Model):
	sender = models.ForeignKey(Pengguna,related_name='sender',on_delete=models.DO_NOTHING)
	recive = models.ForeignKey(Pengguna,related_name='recive',on_delete=models.DO_NOTHING)
	pesan = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created_at']

class RoomChat(models.Model):
	pengirim = models.ForeignKey(Pengguna,related_name='pengirim',on_delete=models.CASCADE)
	penerima = models.ForeignKey(Pengguna,related_name='penerima',on_delete=models.CASCADE)
	kode_chat = models.TextField(unique=True)
