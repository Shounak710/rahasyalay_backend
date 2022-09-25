from rest_framework import serializers
from blog.models import Entry, ENTRY_TYPES


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'title', 'content', 'type', 'entry_datetime', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create and return a new `Entry` instance, given the validated data.
        """
        return Entry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.type = validated_data.get('type', instance.type)
        instance.entry_datetime = validated_data.get('entry_datetime', instance.entry_datetime)
        
        instance.save()
        return instance