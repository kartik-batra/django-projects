from django.shortcuts import render
from .models import SocialAccount, Campaign, Schedule, UserPost
from .serializers import SocialAccountSerializer, CampaignSerializer, ScheduleSerializer, UserPostSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


# Create your views here.

class SocialAccountViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk = None):
        if id is not None:
            stu = SocialAccount.objects.get(user_id = pk)
            serializer = SocialAccountSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = SocialAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    

class CampaignViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk = None):
        if id is not None:
            stu = Campaign.objects.get(campaign_id = pk)
            serializer = CampaignSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ScheduleViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk = None):
        if id is not None:
            stu = Schedule.objects.get(schedule_id = pk)
            serializer = ScheduleSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class UserPostViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk = None):
        if id is not None:
            stu = UserPost.objects.get(user_id = pk)
            serializer = UserPostSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
