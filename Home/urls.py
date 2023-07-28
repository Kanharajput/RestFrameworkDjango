from django.urls import path
from .views import StudentApi
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # it will handle all the requests
    path('',StudentApi.as_view()),
    path('register-user/',views.generateToken),
    # links where a registered user can generate jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]