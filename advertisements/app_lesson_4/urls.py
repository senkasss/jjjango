from django.urls import path
from .views import index, top_sellers



# urlpatterns - обязательное название
urlpatterns = [
    path('index/',index, name = 'main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers')
]