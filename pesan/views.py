from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# Oauth2
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope, TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from base.models import Pengguna, RoomChat, Messages
from pesan.serializer.responeapi import ContactUser, MessageUser

# Home
import json
import uuid


def index(req):
    return render(req,'pesan/dev.html')


class Contact(ListAPIView):
    authentication_classes  = [OAuth2Authentication]
    permission_classes = [IsAuthenticated,TokenHasResourceScope]
    renderer_classes = [JSONRenderer]
    model =Pengguna    
    queryset = Pengguna.objects.all()
    serializer_class = ContactUser

class RoomChatApi(APIView):
    authentication_classes  = [OAuth2Authentication]
    permission_classes = [IsAuthenticated,TokenHasResourceScope]
    renderer_classes = [JSONRenderer]

    def get(self,req):

        if "id-sender" in req.data and "id-recive" in req.data:
            idSender = req.data['id-sender']
            idRecive = req.data['id-recive']
            roomchat = None

            if idRecive is None or idSender is None:
                return Response({'Fields':'Required','status':500},status=500)
            elif type(idRecive) != int or type(idSender) != int:
                return Response({'Fields':'Fields Is Inteeger','status':500},status=500)
            elif idRecive == idSender or idSender == idRecive:
                return Response({'fileds':'Wrong Request','status':500},status=500)

            if RoomChat.objects.filter(pengirim=idSender).first() and RoomChat.objects.filter(penerima=idRecive):
                roomchat = RoomChat.objects.filter(pengirim=idSender).first() or RoomChat.objects.filter(penerima=idRecive)
            elif RoomChat.objects.filter(pengirim=idRecive).first() and RoomChat.objects.filter(penerima=idSender):
                roomchat = RoomChat.objects.filter(pengirim=idRecive).first() or RoomChat.objects.filter(penerima=idSender)        
            else:
                kode = uuid.uuid4()
                roomchat = RoomChat.objects.create(pengirim_id=idSender,penerima_id=idRecive,kode_chat=kode) 


            return Response({'status':200,'KodeRoom':roomchat.kode_chat})
        else:
            return Response({"status":400,"message":"Fields Not Found In Json Request"},status=400)

class DataPesan(ListAPIView):
    authentication_classes  = [OAuth2Authentication]
    permission_classes = [IsAuthenticated,TokenHasResourceScope]
    renderer_classes = [JSONRenderer]
    model = Messages    
    queryset = Messages.objects.all()
    serializer_class = MessageUser

    def get(self,request):
        if "user" in request.data and type(request.data['user']) == int:
            return self.list(request)
        return Response({"status":400,"message":"Wrong Object In Body"},status=400)    

    def get_queryset(self):
        print(self.request.data['user'])
        user = self.request.data['user']
        queryset = Messages.objects.filter(sender=user) | Messages.objects.filter(recive=user)
        return queryset

