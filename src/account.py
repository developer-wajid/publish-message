from all_import import *
from rest_framework import status
from src.serializers import *


class UserLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return JsonResponse({"error": "Please provide both username and password."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is not None:
            # Perform any additional login logic here if needed
            token , _ = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "Login successful.", "token": token.key }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Invalid credentials. Please try again." , "token": ""}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def home_api(request):
    get_user    =   user_profile.objects.get(user=request.user)
    all_messages=messages.objects.filter(company=get_user.company)
    all_vhicles=vehicles.objects.filter(user_profile=get_user)
    allvhicles=VehiclesSerializer(all_vhicles , many=True)

    allmessages = MessagesSerializer(all_messages , many=True)
    return JsonResponse({
                        "all_messages": allmessages.data ,
                        "my_vehicles": allvhicles.data
                        }, 
                        status=status.HTTP_200_OK)






class VehicleAddAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        try:
            get_user = user_profile.objects.get(user=request.user)
            serializer = VehiclesSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save(user_profile=get_user)
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
    def put(self, request, pk, format=None):
        try:
            vehicle = vehicles.objects.get(id=pk)
            serializer = UpdateVehicle(vehicle, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data , status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
    def delete(self, request, pk, format=None):
        try:
            vehicle = vehicles.objects.get(id=pk)
            vehicle.delete()
            return JsonResponse({"message": "Vehicle deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return JsonResponse({'error': str(e)})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def update_vehicle(request, pk):
    try:
        vehicle = vehicles.objects.get(id=pk)
        serializer = UpdateVehicle(vehicle, data=request.data , partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return JsonResponse({'error': str(e)})
    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def delete_vehicle(request):
    try:
        vehicle = vehicles.objects.get(id=request.data['id'])
        vehicle.delete()
        return JsonResponse({"message": "Vehicle deleted successfully"})
    except Exception as e:
        return JsonResponse({'message': str(e)})



class PublishMessageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get(self, request):

        get_user = user_profile.objects.get(user=request.user)
        
        all_messages=messages.objects.filter(company=get_user.company)
        all_vhicles=vehicles.objects.filter(user_profile=get_user)
        
        allvhicles=VehiclesSerializer(all_vhicles , many=True)
        allmessages = MessagesSerializer(all_messages , many=True)
        
        publish_messages = publish_message.objects.filter(user_profile=get_user)
        publishMessages = PublishMessageSerializer(publish_messages, many=True)

        context={
            "all_messages": allmessages.data ,
            "my_vehicles": allvhicles.data ,
            "publishMessages": publishMessages.data

        }
        return JsonResponse(context)
    
    def post(self, request):
        get_user = user_profile.objects.get(user=request.user)
        serializer = PublishMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_profile=get_user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


