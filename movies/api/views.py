from django.shortcuts import render
from rest_framework.views import APIView
from .models import movies,Movies
from .serializer import MovieSerializer,MovieModelSer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# class MovieList(APIView):
#     def get(self,request,*args,**kwargs):
#         allmovies=movies
#         if 'genre' in request.query_params:
#             qp=request.query_params.get("genre")
#             allmovies=[i for i in allmovies if i['genre']==qp]
#         if 'yearlt' in request.query_params:
#             qp=request.query_params.get("yearlt")
#             allmovies=[i for i in allmovies if i['year']<=int(qp)]
#         return Response(data=allmovies)
#     def post(self,request,*args,**kwargs):
#         data=request.data
#         movies.append(data)
#         return Response(data=movies)
    
# class MovieItem(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         movie=[i for i in movies if i['id']==id].pop()
#         # for i in movies:
#         #     if i['id']==id:
#         #         movie=i
#         return Response(data=movie)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         data=request.data
#         movie=[i for i in movies if i['id']==id].pop()
#         movie.update(data)
#         return Response(data=movies)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         movie=[i for i in movies if i['id']==id].pop()
#         movies.remove(movie)
#         return Response(data=movies)
    

#using model and serializer


class MovieList(APIView):
    def get(self,request,*args,**kwargs):
        mvs=Movies.objects.all()
        ser=MovieSerializer(mvs,many=True)
        return Response(data=ser.data)
    def post(self,request,*args,**kwargs):
        mv=request.data
        ser=MovieSerializer(data=mv)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            yr=ser.validated_data.get("year")
            dir=ser.validated_data.get("director")
            genre=ser.validated_data.get("genre")
            Movies.objects.create(name=name,year=yr,director=dir,genre=genre)
            return Response({"msg":"OK"})
        else:
            return Response({"msg":"Movie Adding Failed!!!!"})
    
class MovieItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        mv=Movies.objects.get(id=id)
        ser=MovieSerializer(mv)
        return Response(data=ser.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        mv=Movies.objects.get(id=id)
        mv.delete()
        return Response({"msg":"Deleted"})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        mv=Movies.objects.get(id=id)
        moviedata=request.data
        ser=MovieSerializer(data=moviedata)
        if ser.is_valid():
            mv.name=ser.validated_data.get("name")
            mv.year=ser.validated_data.get("year")
            mv.director=ser.validated_data.get("director")
            mv.genre=ser.validated_data.get("genre")
            mv.save()
            return Response({"msg":"Updated"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
        
#using modelserializer

class MovieMList(APIView):
    def get(self,request,*args,**kwargs):
        mvs=Movies.objects.all()
        dser=MovieModelSer(mvs,many=True)
        return Response(data=dser.data)
    def post(self,request,*args,**kwargs):
        mvs=request.data
        ser=MovieModelSer(data=mvs)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Created"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

class MovieMItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        try:
            mv=Movies.objects.get(id=id)
            dser=MovieModelSer(mv)
            return Response(data=dser.data)
        except:
            return Response({"msg":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        try:
            mv=Movies.objects.get(id=id)
            mv.delete()
            return Response({"msg":"OK"})
        except:
            return Response({"msg":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        mv=Movies.objects.get(id=id)
        ser=MovieModelSer(data=request.data,instance=mv)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Updated"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"registration Completed"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)