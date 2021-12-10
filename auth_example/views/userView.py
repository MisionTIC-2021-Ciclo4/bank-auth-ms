"""
    auth_example/views/userView.py is part of "Demo MisionTIC-2021 C4 - 
    BackendAuthenticationMS", created by Carlos Andrés Sierra.

    "Demo MisionTIC-2021 C4 - BackendAuthenticationMS" is free software: 
    you can redistribute it and/or modify it under the terms of the 
    GNU General Public License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any later version.

    "Demo MisionTIC-2021 C4 - BackendAuthenticationMS" is distributed in 
    the hope that it will be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with "Demo MisionTIC-2021 C4 - BackendAuthenticationMS". 
    If not, see <https://www.gnu.org/licenses/>.

    For contact, you can write to casierrav@unal.edu.co
"""


from rest_framework                          import generics
from auth_example.models.user                import User
from auth_example.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserOtherAccounts(generics.ListAPIView):
    serializer_class   = UserSerializer
    def get_queryset(self):
        queryset = User.objects.exclude(id=self.kwargs['user_id'])
        return queryset


class UserUpdateView(generics.UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)