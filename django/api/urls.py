from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

urlpatterns = [
    # OpenAPI 3 urls
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Stations urls
    path('stations/<int:pk>', views.SpaceStationDetail.as_view()),
    path('stations/', views.SpaceStationList.as_view()),
    # Pointings urls
    path('stations/<int:pk>/state/', views.SpaceStationState.as_view()),
]