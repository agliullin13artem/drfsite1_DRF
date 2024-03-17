from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly




from .models import Category, Women
from .serializers import WomenSerializer

# свой собственный класс пагинации
class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


# чтение  и добавление c ограничением либо авторизованный или только для чтения
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIListPagination


# изменение 
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


# удаление чтение админ и обынчый
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )








# # чиение редлактиирование добаление и тд
# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')

#         if not pk:
#             return Women.objects.all()[:3]
        
#         return Women.objects.filter(pk=pk)


    # новый маршрут
    # @action(method=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get()
    #     return Response({'cats':[cats.name]})
       
    



# # для чтения по GET и добавление по POST запросам все в одном
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# # для измениния данных 
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# # для удаления и чтения данных измениния многов одном
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# class WomenAPIView(APIView):

#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})


#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error: Метод пут не алоовер'})
        
#         try:
#             instance = Women.objects.get(pk=pk)
        
#         except:
#             return Response({'error: Обьект не найден'})


#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    


#     def delete(self, request, *args, **kwargs):
#             pk = kwargs.get('pk', None)
#             if not pk:
#                 return Response({'error: Метод delete не алоовер'})
#             serializer = Women.objects.get(pk=pk).delete

#             return Response({'post':'delete post' + str(pk)})

#         # post_new = Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id'],
#         # )


# создаем первое api
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

