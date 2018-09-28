from .views import CourseList, CourseOne
from django.urls import path, re_path

urlpatterns = [
    path('', CourseList.as_view(), name='all_courses'),
    re_path('^(?P<id>\d+)', CourseOne.as_view(), name='one_course')
]
