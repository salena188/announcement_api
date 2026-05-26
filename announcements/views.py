from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Announcement
from .serializers import AnnouncementSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def announcement_list_create_view(request):

    if request.method == 'GET':
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnnouncementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])
def announcement_detail_view(request, pk):

    try:
        announcement = Announcement.objects.get(pk=pk)

    except Announcement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:

        partial = request.method == 'PATCH'

        serializer = AnnouncementSerializer(
            announcement,
            data=request.data,
            partial=partial
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)