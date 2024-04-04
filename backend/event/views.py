from django.shortcuts import render

from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Event
from .serializers import EventSerializer

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serialized_events = EventSerializer(events, many=True)
        return JsonResponse(serialized_events.data, safe=False)
    elif request.method == 'POST':
        event_data = JSONParser().parse(request)
        serialized_event = EventSerializer(data=event_data)
        if serialized_event.is_valid():
            serialized_event.save()
            return JsonResponse(serialized_event.data, status=201)
        return JsonResponse(serialized_event.errors, status=400)

@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)

    if request.method == 'GET':
        serialized_event = EventSerializer(event)
        return JsonResponse(serialized_event.data)

    elif request.method == 'PUT':
        event_data = JSONParser().parse(request)
        serialized_event = EventSerializer(event, data=event_data)
        if serialized_event.is_valid():
            serialized_event.save()
            return JsonResponse(serialized_event.data)
        return JsonResponse(serialized_event.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'}, status=204)
