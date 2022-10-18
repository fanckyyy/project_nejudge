from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.auth),
    path('reg', views.reg)
]
