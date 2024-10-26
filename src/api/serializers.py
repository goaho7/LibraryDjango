from rest_framework import serializers

from library.models import Author, Book, Tag


class AuthorSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Author
        fields = ("full_name", "birth_date", "death_date", "biography", "tags")


class BookSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Book
        fields = ("title", "publication_date", "genre", "description", "author", "tags")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("name", "description")
        model = Tag
