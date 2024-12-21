from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

dataset = {}

def generate_id() -> int:
    if dataset:
        return max(dataset.keys()) + 1
    return 1

@api_view(['POST', 'GET'])
def items(request):
    if request.method == 'POST':
        data = request.data
        new_id = generate_id()
        dataset[new_id] = data
        return Response({"id": new_id, "item": data}, status=201)

    if request.method == 'GET':
        return Response(dataset)
    
@api_view(['GET', 'PUT', 'DELETE'])
def item(request):
    pass