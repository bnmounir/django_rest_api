from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_app import serializers, models, permissions
# Create your views here.


class HelloApiView(APIView):
    ''' test API View '''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' returns a list of API View Features '''
        an_apiview = [
            'Uses http methods', 'get', 'post', 'put', 'patch', 'delete'
        ]
        return Response({
            'message': 'Serving the api list',
            'api_view': an_apiview
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''handles updating by replacing an objects'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''handles updating on field an objects'''
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        '''handles delete an objects'''
        return Response({'method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    ''' test api view '''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        ''' return hello message '''

        a_viewset = ['view one', 'view two', 'view three']

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        ''' create message '''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        ''' retrive an object '''
        return Response({'http_method': 'retrive  GET'})

    def update(self, request, pk=None):
        ''' retrive an object '''
        return Response({'http_method': 'update put style'})

    def partial_update(self, request, pk=None):
        ''' retrive an object '''
        return Response({'http_method': 'update patch style'})

    def destroy(self, request, pk=None):
        ''' retrive an object '''
        return Response({'http_method': 'destroy delete style'})


class UserProfileViewSet(viewsets.ModelViewSet):
    ''' handle updating profile'''

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    ''' handle auth token '''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    ''' handle crud feed functions '''
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permissions_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        ''' set user profile to logged user '''
        serializer.save(user_profile=self.request.user)
