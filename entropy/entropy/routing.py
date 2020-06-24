from channels.routing import ProtocolTypeRouter, URLRouter
from app.routing import websocket

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': URLRouter(websocket)
})