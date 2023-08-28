from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework import status
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication, TokenAuthentication



# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'Movies': 'Welcome To My Movie API'})

@permission_classes([AllowAny])
@api_view(['GET'])
@cache_page(60 * 15)
def GetAllMovies(request):
    paginator = PageNumberPagination()
    queryset = Movie.objects.all()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    
    serializer = MovieSerializer(paginated_queryset, many=True)
    response_data = {
        'count': paginator.page.paginator.count,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'results': serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@api_view(['POST'])
@swagger_auto_schema(
    tags=['Movies'],
    operation_summary="Create a new movie",
    request_body=openapi.Schema(  # Request body schema
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'lead_actor': openapi.Schema(type=openapi.TYPE_STRING),
            'release_year': openapi.Schema(type=openapi.TYPE_INTEGER),
            
        },
        required=['title'],
    ),
    responses={201: 'Created'},
)
def CreateMovie(request): 
    data = request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Success': 'The movie was successfully created'}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@api_view(['DELETE'])
@cache_page(60 * 15)
def DeleteMovie(request):
    movie_id = request.data.get('movie_id')
    try:
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return Response( {'Success': 'The movie was successfully deleted'}, status=201)
    except Movie.DoesNotExist:
        return Response( {'Error': 'The movie does not exist'}, status=400)

@permission_classes([AllowAny])
@api_view(['GET'])
@cache_page(60 * 15)
def GetMovie(request):
    movie_id = request.data.get('movie_id')
    try:
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response( {'Error': 'The movie does not exist'}, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@cache_page(60 * 15)
def UpdateMovie(request):
    movie_id = request.data.get('movie_id')
    get_new_title = request.data.get('new_title')
    get_new_lead_actor = request.data.get('new_lead_actor')
    get_new_release_year = request.data.get('new_release_year')

    if not movie_id:
        return Response({'Error': 'movie_id is required'}, status=400)

    try:
        movie = Movie.objects.get(id=movie_id)
        
        if get_new_title is not None:
            movie.title = get_new_title
        if get_new_lead_actor is not None:
            movie.lead_actor = get_new_lead_actor
        if get_new_release_year is not None:
            movie.release_year = get_new_release_year
        
        movie.save()
        
        return Response({'Success': 'The movie was successfully updated'}, status=200)
        
    except Movie.DoesNotExist:
        return Response({'Error': 'The movie does not exist'}, status=404)


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user to register
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required.'}, status=400)

    hashed_password = make_password(password)
    user = User.objects.create(username=username, password=hashed_password)
    return Response({'message': 'User registered successfully.'}, status=201)

