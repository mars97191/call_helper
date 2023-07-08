from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]