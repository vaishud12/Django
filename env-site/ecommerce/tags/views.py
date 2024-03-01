from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.response import Response 
from tags.serializers import CreateTagSerializer, ReadTagSerializer
from tags.models import Tag 
from rest_framework import status, throttling
from django.utils.text import slugify
from tags.filters import StandardResultsSetPagination, CustomThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.cache import cache
from tags.permissions import CustomerPermission
from authentication.permissions import IsAuthenticated, IsAdmin

# Create your views here.

class CreateTag(APIView):
    permission_classes = (IsAdmin,)
    def post(self,request):
        print("auth user" ,request.user)
        create_serializer = CreateTagSerializer(data=request.data)
        if create_serializer.is_valid():
            name = create_serializer.validated_data.get('name')
            tag_object = Tag.objects.create(
                name=name,
                slug=slugify(name)
            )
            response_data = ReadTagSerializer(instance=tag_object).data 
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            return Response(create_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#simple api view
class ListTagV1(APIView):
    def get(self,request):
        queryset = Tag.objects.all()
        response_data = ReadTagSerializer(queryset, many=Tag).data
        return Response(response_data, status=status.HTTP_200_OK)

#createdapi
class ListTagV2(ListAPIView):
    queryset=Tag.objects.all()
    #_class means a single class
    serializer_class=ReadTagSerializer
    #_class means single class
    pagination_class= StandardResultsSetPagination #it used to render the that must object the page no is given
    #classes: multiple classes tuple of classes
    throttle_classes=(CustomThrottle,)
    #filters
    filter_backends = [DjangoFilterBackend]
    filter_backends=[filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields=['name',]
    ordering_fields=['created_at']
    filterset_fields=['slug']

    def get_queryset(self):
        return Tag.objects.all()
#in case you want to add single none classes
#pagination_classes= none
#in case you want to add multiple none classes
authentication_classes=[]

class TagDetail(APIView):
    def get(self,request,slug):
        print('slug',slug)
        try:
            tag_object=Tag.objects.get(slug=slug)
        except Tag.DoesNotExist:
            error_response={"error":True, "message":"tags does not exist"}
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
        except Tag.MultipleObjectsReturned:
            error_response={"error":True, "message":"multiple tags exist"}
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
        response_data=ReadTagSerializer(instance=tag_object).data
        return Response(response_data, status=status.HTTP_200_OK)

class TagDetailV2(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = ReadTagSerializer
    lookup_field='id'