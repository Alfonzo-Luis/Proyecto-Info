from django.urls import path
from .views import user_login, user_logout
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('registro/', views.Registro.as_view(), name='registro')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)