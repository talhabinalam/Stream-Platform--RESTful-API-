from django.urls import path
from .views import *

urlpatterns = [
    # path('movies/', movies, name='movies'),
    # path('movies/<int:id>', movie_details, name='movies_details'),
    path('watchlist/', WatchListView.as_view(), name='watchlist'),
    path('watchlist/<int:pk>/', WatchListDetailsView.as_view(), name='watchlist-details'),
    path('stream/', StreamPlatformView.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamDetailsView.as_view(), name='stream-details'),

    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]



