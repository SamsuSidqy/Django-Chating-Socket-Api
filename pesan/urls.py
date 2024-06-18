from django.urls import path

from . import views

urlpatterns = [
	path('dev/',views.index),
	path('contact/',views.Contact.as_view()),
	path('room/',views.RoomChatApi.as_view()),
	path('message/',views.DataPesan.as_view()),
]