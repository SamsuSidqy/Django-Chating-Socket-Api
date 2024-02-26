from django.urls import path
from .consumers import(
		ChattingSocket,		
	)

urlpattern_socket = [
	path('chat/<str:room>/',ChattingSocket.as_asgi()),
]