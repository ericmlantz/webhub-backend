from rest_framework import serializers
from .models import User, Interest, Search, Page, Note

class UserSerializer(serializers.HyperlinkedModelSerializer):
    interests = serializers.HyperlinkedRelatedField(
        view_name='interest_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = User
       fields = ('id', 'name', 'email', 'password', 'interests')

class InterestSerializer(serializers.HyperlinkedModelSerializer):
    pages = serializers.HyperlinkedRelatedField(
        view_name='page_detail',
        many=True,
        read_only=True
    )
    searches = serializers.HyperlinkedRelatedField(
        view_name='search_detail',
        many=True,
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user')

    class Meta:
       model = Interest
       fields = ('id', 'topic', 'description', 'pages', 'searches', 'user_id')

class SearchSerializer(serializers.HyperlinkedModelSerializer):
    interest = serializers.HyperlinkedRelatedField(
        view_name='interest_detail',
        read_only=True
    )

    interest_id = serializers.PrimaryKeyRelatedField(
    queryset=Interest.objects.all(),
    source='interest')

    class Meta:
       model = Search
       fields = ('id', 'query', 'results', 'interest', 'interest_id')

class PageSerializer(serializers.HyperlinkedModelSerializer):
    interest = serializers.HyperlinkedRelatedField(
        view_name='interest_detail',
        read_only=True
    )
    notes = serializers.HyperlinkedRelatedField(
        view_name='note_detail',
        many=True,
        read_only=True
    )

    interest_id = serializers.PrimaryKeyRelatedField(
    queryset=Interest.objects.all(),
    source='interest')

    class Meta:
       model = Page
       fields = ('id', 'title', 'url', 'interest', 'interest_id', 'notes')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    page = serializers.HyperlinkedRelatedField(
        view_name='page_detail',
        read_only=True
    )

    page_id = serializers.PrimaryKeyRelatedField(
    queryset=Page.objects.all(),
    source='page')

    class Meta:
       model = Note
       fields = ('id', 'title', 'content', 'page', 'page_id')