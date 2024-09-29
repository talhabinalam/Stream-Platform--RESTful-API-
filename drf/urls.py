from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('account/', include('accounts.urls')),
    path('auth-api/', include('rest_framework.urls')),
]
