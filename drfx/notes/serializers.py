from .models import Notes
from users import serializers
from rest_framework import serializers 

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = (
            "created_on",
            "updated_on",
            "is_deleted",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        note_type = request.data.get('note_type') if request else None

        if note_type == 'text':
            self.fields['audio_file'].read_only = True
            self.fields['video_file'].read_only = True
        elif note_type == 'audio':
            self.fields['text_content'].read_only = True
            self.fields['video_file'].read_only = True
        elif note_type == 'video':
            self.fields['text_content'].read_only = True
            self.fields['audio_file'].read_only = True
