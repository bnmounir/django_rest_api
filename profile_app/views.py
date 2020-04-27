from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    ''' test API View '''
    def get(self, request, format=None):
        ''' returns a list of API View Features '''
        an_apiview = [
            'Uses http methods', 'get', 'post', 'put', 'patch', 'delete'
        ]
        return Response({
            'message': 'Serving the api list',
            'api_view': an_apiview
        })
