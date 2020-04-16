from SingleSignOn.response import Response
from SingleSignOn.request import Request

class MyService():

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle(self, request, sso_token):
        if self.sso_registry.is_valid(sso_token):
            return Response(f"Hello {request.name}")
        else:
            return  Response("Please sign in")


