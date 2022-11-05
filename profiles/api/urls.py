from django.urls import path
from .views import ProfileList


urlpatterns = [
    path("user-profiles/", ProfileList.as_view(), name='profiles'),
]
