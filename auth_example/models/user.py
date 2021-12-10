"""
    auth_example/models/user.py is part of "Demo MisionTIC-2021 C4 - 
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


from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

# Manager to handle type of DjangoUsers, not the same as ApplicationRoles.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("El cliente debe tener un username.")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username = username, 
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id        = models.BigAutoField(primary_key=True)
    username  = models.CharField('Username', max_length=20, unique=True)
    password  = models.CharField('Password', max_length=256)
    name      = models.CharField('Name',     max_length=50)
    email     = models.EmailField('Email',   max_length=100, unique=True)
    time_zone = models.CharField('TimeZone', max_length=50, default="America/Bogota")

    def save(self, **kwargs):
        '''
        This function is created cos' we need to encrypt password
        before save user into the database.
        '''
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects        = UserManager()
    USERNAME_FIELD = 'username'