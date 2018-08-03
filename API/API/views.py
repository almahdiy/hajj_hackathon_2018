
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import TrafficLight
from .serializers import TrafficLightSerializer
#from random import randint
#from operator import itemgetter
import requests
#import base64
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST', ])
# def parent_login_attempt(request):
#     """
    
#     if(request.method == 'POST'):
#         #data is a dictionary that has the username and the password the user tried
#         data = ParentSerializer(request.data).data
#         u = data["username"]
#         p = data["password"]
#         try:
#             #SELECT parent FROM Parent WHERE username=u, password = p;
#             q = Parent.objects.get(username=u, password=p)
#             parent_id = ParentSerializer(q).data['id']
#             #will return an exception if not found, hence the try/except block.
#             return Response(parent_id)
#         except:
#             return Response(None)


class TrafficLightList(APIView):
    """
    List all traffic lights, or add a new traffic light to the database.
    """
    def get(self, request, format=None):
        #print("Test 1")
        traffic_light = TrafficLight.objects.all()
        #print("Test 2")
        serializer = TrafficLightSerializer(traffic_light, many=True)
        #print("Test 3")
        return Response(serializer.data)

    def post(self, request, format=None):
        #print(request.data)
        if(type(request.data) is list):
            for item in request.data:
                serializer = TrafficLightSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = TrafficLightSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrafficLightDetails(APIView):
    """
    access a specific Parent object, edit it, and delete it.
    """
    def get_object(self, pk):
        try:
            return TrafficLight.objects.get(pk=pk)
        except TrafficLight.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        traffic_light = self.get_object(pk)
        serializer = TrafficLightSerializer(parent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        traffic_light = self.get_object(pk)
        serializer = TrafficLightSerializer(traffic_light, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        traffic_light = self.get_object(pk)
        traffic_light.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_statuses(request):
    """
    Docstring
    """
    if(request.method == 'GET'):
        #print("Type: {}".format(TrafficLight.objects.all()))
        #SELECT child FROM Child WHERE parent_id = pk;
        #print("size here: {}".format(len(list(TrafficLight.objects.all()))))
        temp = list(TrafficLight.objects.all())[:15]
        #print("Original size: {}\nlist: {}\nRemaining: {}".format(len(list(TrafficLight.objects.all())), temp, list(TrafficLight.objects.all())[15:]))
        
        
        q = [TrafficLightSerializer(x).data for x in temp]
        result = []
        for i in range(len(q)):
            s = ((q[i]["persons"]*1.5)*100)/q[i]["area"]
            if(s <= 49 and s >= 0):
                result.append({"lng": q[i]["lng"], "lat": q[i]["lat"], "status": "greenLights"})
            elif(s >= 50 and s <= 74):
                result.append({"lng": q[i]["lng"], "lat": q[i]["lat"], "status": "yellowLights"})
            else:
                result.append({"lng": q[i]["lng"], "lat": q[i]["lat"], "status": "redLights"})

        for item in temp:
            #print(TrafficLightSerializer(item).data)
            item2 = TrafficLight.objects.get(pk=TrafficLightSerializer(item).data["id"])
            #print("We here?")
            item2.delete()

        return Response(result)