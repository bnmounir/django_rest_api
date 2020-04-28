from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_app import serializers
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
