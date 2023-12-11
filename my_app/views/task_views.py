from .imports import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TaskIndex(request):
    try:
        task = TaskModel.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(task, request)
        seri = TaskSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TaskStore(request):
    seri = TaskSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TaskShow(request, pk):
    try:
        task = TaskModel.objects.get(pk=pk)
        seri = TaskSerializer(task)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def TaskUpdate(request, pk):
    try:
        task = TaskModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = TaskSerializer(task, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def TaskDelete(request, pk):
    try:
        task = TaskModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    task.delete()
    return Response({"message":"Deleted Successfully"},status=200)