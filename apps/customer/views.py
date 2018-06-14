from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes

from apps.customer.serializers import UserSerializer
from apps.address.models import Province, City

User = get_user_model()


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def sign_up(request):
    response = {
        'error':True,
        'msg':'Parámetros erroneos',
        'data':{}
    }

    # Get data
    data = request.POST

    try:
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        first_name = request.data['first_name']
        last_name = request.data['last_name']
        
        province = request.data['province']
        city = request.data['city']
        sector = request.data['sector']
        phone = request.data['phone']

        # Check for email
        user = User.objects.filter(email=email).first()
        if user:
            response['msg'] = 'El correo ya se encuentra registrado!'
            return JsonResponse(response)

        # Create user
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)

        user.phone = phone
        user.phone = phone

        user.province = Province.objects.get(id=province)
        user.city = City.objects.get(id=city)
        user.sector = sector

        user.save()

        # Serializer User
        serializer = UserSerializer(user)
        user = serializer.data

        response['error'] = False
        response['msg'] = 'Usuario registrado correctamente'
        response['data'] = user
    except Exception as e:
        response['msg'] = str(e)

    return JsonResponse(response)
