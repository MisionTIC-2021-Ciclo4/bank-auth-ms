"""
    bank_auth_example/urls.py is part of "Demo MisionTIC-2021 C4 - 
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

from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views

urlpatterns = [
    path('',                                   views.UserWelcomeView.as_view()),
    path('admin/',                             admin.site.urls),
    path('login/',                             TokenObtainPairView.as_view()),
    path('refresh/',                           TokenRefreshView.as_view()),
    path('verifyToken/',                       views.VerifyTokenView.as_view()),
    path('user/',                              views.UserCreateView.as_view()),
    path('user/<int:pk>/',                     views.UserDetailView.as_view()),
    path('user/update/<int:pk>/',              views.UserUpdateView.as_view()),
    path('user/delete/<int:pk>/',              views.UserDeleteView.as_view()),
    path('user/other_accounts/<int:user_id>/', views.UserOtherAccounts.as_view()),
]
