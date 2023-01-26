from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from base.models import Person
from .serializers import ItemSerializer
from .serializers import PersonSerializer
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def addItem(request):
    serializier = ItemSerializer(data=request.data)
    if serializier.is_valid():
        serializier.save()
    return Response(serializier.data)

@api_view(['GET'])
def getPerson(request):
    persons = Person.objects.all()
    serializer2 = PersonSerializer(persons, many=True)
    return Response(serializer2.data)

@api_view(['PUT'])
def addPerson(request):
    serializier2 = PersonSerializer(data=request.data)
    if serializier2.is_valid():
        serializier2.save()
    return Response(serializier2.data)