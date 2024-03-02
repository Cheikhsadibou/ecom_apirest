from rest_framework import serializers
from watchlist_app.models import Review, StreamPlatform, WatchList 
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    # review_user = serializers.StringRelatedField()
    review_user = serializers.StringRelatedField(read_only=True)

    # def create(self, validated_data):
    #     user_dict = validated_data.pop('review_user')
    #     user_obj, created = User.objects.get_or_create(**user_dict)
    #     return Review.objects.create(user=user_obj, **validated_data)

    class Meta:
        model = Review
        # exclude = ('watchlist',)
        # fields = "__all__"
        fields = ('id','review_user', 'rating', 'description','active','created','updated')

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    plateform = serializers.CharField(source='plateform.name')
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ('id','platform', 'title', 'storyline', 'plateform', 'active', 'reviews', 'avg_rating','number_rating', 'created')
        
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        # fields = ['url', 'id', 'name', 'about', 'website']
        
