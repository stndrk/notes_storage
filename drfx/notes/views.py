from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from notes.models import Notes
from notes.serializers import NotesSerializer

class NoteCreateView(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    parser_classes = (MultiPartParser, FormParser)

    # def create(self, request, *args, **kwargs):
    #     note_type = request.data.get('note_type')

    #     serializer = self.get_serializer(data=request.data) 
    #     serializer.is_valid(raise_exception=True)

    #     serializer.context['note_type'] = note_type

    #     self.perform_create(serializer)

    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        note_type = self.request.data.get('note_type')
        serializer.save(user=self.request.user, note_type=note_type)







