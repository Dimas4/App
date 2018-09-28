from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile/', include('profile_model.urls')),
    path('api/course/', include('course_model.urls'))
]
