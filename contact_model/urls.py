from django.urls import path, re_path, include


urlpatterns = [
    re_path('^(?P<id>\d+)', ProfileOne.as_view(), name='one_profile')

]
