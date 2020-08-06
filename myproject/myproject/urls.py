"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views



from  rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', views.teacherlist.as_view()),
    path('student/', views.studentlist.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    path('api/jwt/',TokenObtainPairView.as_view()),

    path('api/jwt/refresh/',TokenRefreshView.as_view())
]
