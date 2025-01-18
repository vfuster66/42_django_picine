from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajoutez cette ligne
    path('account/', include('account.urls')),
    path('chat/', include('chat.urls')),
]
