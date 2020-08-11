# from core.serializers import UserSerializer
import json

# def my_jwt_response_handler(token, user=None, request=None):
#     return {
#         'token': token,
#          # 'user': UserSerializer(user, context={'request': request}).data

#      }
def john (token, user=None, request=None):
    return {
        'token': token,
         # 'user': UserSerializer(user, context={'request': request}).data

     }
