from rest_framework import serializers
from rk.models import Computer, Program

class ComputerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    cost = serializers.IntegerField()
    class Meta:
        model = Computer
        fields =[
            'id', 'name', 'cost'
        ]

class ProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    computer_id = serializers.IntegerField()

    class Meta:
        model = Program
        fields =[
            'id', 'name','size', 'computer_id'
        ]