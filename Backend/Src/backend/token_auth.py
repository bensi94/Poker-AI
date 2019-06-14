from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        tokenString = scope['query_string']
        try:
            token_name, token_key = tokenString.decode().split('=')
            if token_name == 'Token':
                token = Token.objects.get(key=token_key)
                scope['user'] = token.user
        except Token.DoesNotExist:
            pass
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))
