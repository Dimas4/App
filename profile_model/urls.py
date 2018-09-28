from .views import ProfileList, ProfileOne
from django.urls import path, re_path

urlpatterns = [
    path('', ProfileList.as_view(), name='all_profiles'),
    re_path('^(?P<id>\d+)', ProfileOne.as_view(), name='one_profile')
]
