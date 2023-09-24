# artistapp/views.py
from rest_framework import filters 
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this endpoint

    def perform_create(self, serializer):
        serializer.save()

class ArtistFilterListView(generics.ListAPIView):
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        artist_name = self.request.query_params.get('artist')
        return Artist.objects.filter(name__icontains=artist_name)

class ArtistRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow registration for any user

    def post(self, request):
        # Create a new User object
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        # Create a corresponding Artist object using signals

        # Create a new token for the user
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
