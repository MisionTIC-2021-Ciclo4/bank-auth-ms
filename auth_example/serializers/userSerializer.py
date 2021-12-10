"""
    auth_example/serializers/userSerializer.py is part of Demo MisionTIC-2021 C4, 
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

from auth_example.models.user import User
from rest_framework           import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'name', 'email']


    def to_representation(self, obj):
        '''
        DataStructure to return the information for any user when
        a request asked it.
        '''
        user    = User.objects.get(id=obj.id)
        return {
            'id'       : user.id,
            'username' : user.username,
            'name'     : user.name,
            'email'    : user.email,
            'timeZone' : user.time_zone,
        }