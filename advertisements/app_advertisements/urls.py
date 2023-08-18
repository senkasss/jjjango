from django.urls import path
from .views import index
from .views import ind


# urlpatterns - обязательное название
urlpatterns = [
    path('', index), path('', ind)
]