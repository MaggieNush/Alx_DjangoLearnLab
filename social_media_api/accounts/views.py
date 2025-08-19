from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .serializers import RegistrationSerializer, CustomUserSerializer

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    # Automatically handles user creation
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [] # No permission needed for registration

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Get the created user and create a token for them
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
    
class LoginView(APIView):
    permission_classes = [] # No permission needed for login

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user against the database
        user = authenticate(username=username, password=password)

        if user:
            # Get or create a token and return it if a user is authenticated successfully
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        else:
            # If authentication fails, return an error
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(APIView):
    # This view requires a token for authentication
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
