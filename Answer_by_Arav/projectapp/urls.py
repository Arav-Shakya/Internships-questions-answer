
from django.contrib import admin
from django.urls import path, include
from Answer.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Answer.urls')),
    path('', index, name="index"),
]
