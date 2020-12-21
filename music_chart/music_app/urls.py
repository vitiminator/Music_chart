from django.urls import path

from .views import SongLook, ChartLook

app_name = 'chart'

urlpatterns = [
    path('chart/', ChartLook.as_view(), name='chart'),
    path('chart/<str:author>/', SongLook.as_view(), name='song')
]