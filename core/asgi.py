import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import pesan.ChannelsBackend.routing as route


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
		"http":get_asgi_application(),
		"websocket":AllowedHostsOriginValidator(
			AuthMiddlewareStack(URLRouter(route.urlpattern_socket))
		)
})