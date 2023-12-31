"""BuildApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.authtoken import views
from django.urls import path,include
from rest_framework_simplejwt.views import (    
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('nested-serializer/',include('AnotherApp.urls')),
    path('api-auth-token/',views.obtain_auth_token),            # expose this url so that user can create their token
    # links where a registered user can generate jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate-pdf/',include('GeneratePdf.urls')),
    path('otp/',include('OtpApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)