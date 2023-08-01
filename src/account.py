from all_import import *
from rest_framework import status



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






    
    



