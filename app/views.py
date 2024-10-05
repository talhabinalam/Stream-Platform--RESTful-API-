import logging

# from rest_framework import mixins
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

from .serializers import *
from .permissions import *
from .throttling import *

logger = logging.getLogger(__name__)

# def movies(request):
#     movie_list = Movie.objects.all()
#     # print(movie_list.values())
#     data = {'Movie': list(movie_list.values())}
#
#     print(data)
#
#     return JsonResponse(data)


# def movie_details(request, id):
#     movie = Movie.objects.get(id=id)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     print(data)
#     return JsonResponse(data)


# @api_view(['GET', 'POST'])
# def movies(request):
#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     movie_list = Movie.objects.all()
#     serializer = MovieSerializers(movie_list, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Exception:
#         return Response({'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
#
#
#     if request.method == 'GET':
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = MovieSerializers(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'message': 'Movie has been deleted'}, status=200)



class WatchListView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializers(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailsView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializers(movies)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializers(movies, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)



class StreamPlatformView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(platform, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StreamDetailsView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ReviewDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class ReviewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-list'


    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

    def perform_create(self, serializer):
        current_user = self.request.user
        if not current_user.is_authenticated:
            raise ValidationError("Please login first")
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk) # Query specific movie and store it in watchlist
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=current_user)
        if review_queryset.exists():
            raise ValidationError("Review already exists")

        if watchlist.total_review == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
        watchlist.total_review = watchlist.total_review + 1

        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=current_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
