from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from autentikasi.Serialisasi.Pengguna import PenggunaSerilisasi
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from datetime import datetime   

# Model
from base.models import Pengguna

# Oauth2
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope, TokenHasScope, OAuth2Authentication
from oauth2_provider.models import AccessToken
from oauthlib.common import generate_token 


class RegisterApi(CreateAPIView):   
    serializer_class = PenggunaSerilisasi
    renderer_classes = [JSONRenderer]
    allowed_methods = 'POST'
    def create(self,req,*args,**kwargs):
        serializer = self.serializer_class(data=req.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer)
        return Response(serializer.data, status=200, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Message':  data[api_settings.URL_FIELD_NAME]}
        except Exception as e:
            return {'Errors':e}

class LoginApi(APIView):    
    renderer_classes = [JSONRenderer]

    def post(self,req):

        if req.data['username'] is None or req.data['password'] is None:
            return Response({'status':500,'Message':'Username And Password Required'})

        obj = Pengguna.objects.filter(username=req.data['username']).first()

        # Cek Jika Query Username Tidak Di Temukan
        if obj is None:
            return Response({'status':404,'Message':'Username Atau Password Tidak Di Temukan'}) 
        pswd = obj.password
        cekPassword = check_password(req.data['password'],pswd) 

        # Cek Jika Password Tidak Correct
        if cekPassword is False:
            return Response({'status':500,'Message':'Password Atau Username Salah'})

        checkingToken = AccessToken.objects.filter(user=obj)
        # Cek Sudah Ada Token or Not
        if checkingToken:
            return Response({'Status':500,'Message':'Anda Sudah Login'})
        token = generate_token()
        createToken = AccessToken.objects.create(user=obj,expires=datetime(2024,5,20),token=token)        
        serializer = PenggunaSerilisasi(obj)       
        data = {
            'status':200,
            'data':serializer.data,
            'token':createToken.token,
            'expires':createToken.expires,
            'token_created_at':createToken.created
        }
        return Response(data) 

class CekAuth(APIView):    
    authentication_classes  = [OAuth2Authentication]
    permission_classes = [IsAuthenticated,TokenHasResourceScope]

    def get(self,req):
        return Response({'Pesan':'Berhasil'})


class LogoutApi(APIView):
    authentication_classes  = [OAuth2Authentication]
    permission_classes = [IsAuthenticated,TokenHasResourceScope]
    renderer_classes = [JSONRenderer]

    def post(self,req):
        cekToken = AccessToken.objects.filter(token=req.data['token'])
        if cekToken:
            cekToken.delete()
            return Response({"status":200,"message":"Logout Berhasil"})

        return Response({"status":500,"message":"Gagal Logout"})



