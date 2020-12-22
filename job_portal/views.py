from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *
from .models import Job


class JobApplicantViewSet(viewsets.ModelViewSet):
    queryset = JobApplicant.objects.all()
    serializer_class = JobApplicantSerializer

class JobsViewSet(APIView):

    def get(self, request, format=None):
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class JobViewSet(APIView):

    def get_object(self, id):
        try:
            return Job.objects.get(pk=id)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        job = self.get_object(id)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        job = self.get_object(id)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        job = self.get_object(id)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobApply(APIView):

    def get_object(self, id):
        try:
            return Job.objects.get(pk=id)
        except Job.DoesNotExist:
            raise Http404

    def post(self, request, id, format=None):
        request.data['job_id'] = id
        serializer = JobApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

