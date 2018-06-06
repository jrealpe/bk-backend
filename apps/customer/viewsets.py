from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.customer.serializers import UserSerializer

from fcm_django.models import FCMDevice


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        """
            Login
            Ex:
                request  --> {
                    'username': <username string>,
                    'password': <password string>,
                    'device': {
                        'name': <device_name string>,
                        'regstration_id': <fcm_token string>,
                        'type': <type string> 
                    }
                }
                response --> {
                    'is_error': True/False,
                    'msg': <msg string>,
                    'data': {
                        'user': <user object>
                    }
                }
        """
        response = {'is_error': False}
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
        except:
            response['is_error'] = True
            response['msg'] = 'Usuario y contraseña incorrectos'
            return Response(response)

        try:
            # Get user
            user = serializer.validated_data['user']
            
            # Get or create device
            device = data.get('device', None)
            device['user'] = user
            device = FCMDevice.objects.get_or_create(**device)

            # Get or create token
            token, created = Token.objects.get_or_create(user=user)

            # Serialize user
            serializer = UserSerializer(
               user,
               context={
                  'request': request,
                  'token': token.key
               })
            user = serializer.data

            response['msg'] = 'Se ha iniciado sesión correctamente'
            response['data'] = user
        except Exception as e:
            response['is_error'] = True
            response['msg'] = 'Ha ocurrido un error, intente nuevamente'

        return Response(response)
