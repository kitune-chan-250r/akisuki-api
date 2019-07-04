from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import CountDataViewSet


router = routers.DefaultRouter()
router.register(r'count', CountDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]