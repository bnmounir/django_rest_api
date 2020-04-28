from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    ''' serializer like form takes and validates inputs '''
    name = serializers.CharField(max_length=10)