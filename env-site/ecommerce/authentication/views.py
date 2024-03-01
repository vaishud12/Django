from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import CreateUserSerializer

class SignUpView(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self, request):
        create_serializer = CreateUserSerializer(data=request.data)
        if create_serializer.is_valid():
            username = create_serializer.validated_data.get('username')
            email = create_serializer.validated_data.get('email')
            password = create_serializer.validated_data.get('password')

            if User.objects.filter(username=username).exists():
                return Response({'error': True, 'error_msg': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                return Response({'error': True, 'error_msg': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({"success": True, "success_msg": "Try logging in with the same credentials"})
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
