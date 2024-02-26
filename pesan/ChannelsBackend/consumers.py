from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
import json


from base.models import Messages


class ChattingSocket(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']
        room = self.scope['url_route']['kwargs']['room']
        print(self.scope)
        self.room_group_name= room
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

        await self.accept()

    async def receive(self,text_data):
        data = json.loads(text_data)
        user = self.scope['user']
        await self.save_message(data)   
        await self.channel_layer.group_send(
                self.room_group_name,{
                    'type' : 'chatPesan',
                    'message':data['message'],
                    'id_sender':data['id_sender'],
                    'id_recive':data['id_recive'], 
                }
            )

    async def chatPesan(self,event):

        await self.send(text_data=json.dumps({
                'type':'chat',
                'status':'200',
                'message':event['message'],
                'id_kirim':event['id_sender'],
                'id_terima':event['id_recive'],  

            }))
    @database_sync_to_async 
    def save_message(self,data):
        id_sender = data['id_sender']
        id_recive = data['id_recive']
        konten = data['message']
        return Messages.objects.create(sender_id=id_sender,recive_id=id_recive,pesan=konten)
