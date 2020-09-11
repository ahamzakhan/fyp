
from django.contrib import admin
from django.urls import path, include
from users import views as users_views

urlpatterns = [

    path('admin/', admin.site.urls),
   	path('', include('studentmodule.urls')),
]
