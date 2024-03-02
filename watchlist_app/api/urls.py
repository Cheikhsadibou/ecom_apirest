from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import (
                                    StreamPlatformVS, 
                                    ReviewCreate, 
                                    ReviewDetail, 
                                    ReviewList, 
                                    StreamPlatformDetailAV, 
                                    UserReview, WatchListAV, 
                                    WatchDetailAV, 
                                    StreamPlatformAV, 
                                    WatchListGV
                                )
# from watchlist_app.models import StreamPlatform 

router = DefaultRouter()
router.register('stream_platforms', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watchlist-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    path('', include(router.urls)),
    # path('stream_platforms/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    # path('stream_platforms/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review_create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail'),
    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
]
