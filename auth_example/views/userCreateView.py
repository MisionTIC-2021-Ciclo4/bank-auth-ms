"""
    auth_example/views/userCreateView.py is part of Demo MisionTIC-2021 C4, 
    created by Carlos Andrés Sierra.

    Demo MisionTIC-2021 C4 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Demo MisionTIC-2021 C4 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Demo MisionTIC-2021 C4. If not, see <https://www.gnu.org/licenses/>.

    For contact, you can write to casierrav@unal.edu.co
"""


from rest_framework                          import status, views
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from auth_example.serializers.userSerializer import UserSerializer

class UserWelcomeView(views.APIView):
    def get(self, request, *args, **kwargs):
        message = {"Detail" : "Welcome to AuthMS."}
        return Response(message, status=status.HTTP_200_OK)

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token_data       = {"username":request.data['username'],
                            "password":request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)