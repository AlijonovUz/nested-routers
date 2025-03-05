from rest_framework import viewsets

from .serializers import GroupSerializer, ChapterSerializer
from .models import Group, Chapter


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.filter(group_id=self.kwargs.get('group_pk'))
