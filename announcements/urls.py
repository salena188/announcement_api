from django.urls import path
from .views import (
    announcement_list_create_view,
    announcement_detail_view
)

urlpatterns = [
    path('', announcement_list_create_view),
    path('<int:pk>/', announcement_detail_view),
]