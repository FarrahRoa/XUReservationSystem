from django.urls import path
from Room_Booking import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.api_root,name="api-root"),
    path("rooms/",views.RoomList.as_view(),name="room-list"),
    path('rooms/<int:pk>', views.RoomDetail.as_view(),name="room-detail"),
    path('occupied-dates/',views.OccupiedDatesList.as_view(),name="occupiedDates"),
    path('occupied-dates/<int:pk>',views.OccupiedDatesDetail.as_view(),name="occupiedDates"),
]

urlpatterns = format_suffix_patterns (urlpatterns)

from django.conf import settings
from django.conf import static

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)