from rest_framework import serializers
from .models import *

# def validate_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
# def validate_description(value):
#     if value.upper():
#         raise serializers.ValidationError("Description should be lower case")
#
#
# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_name])
#     description = serializers.CharField(validators=[validate_description])
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance


class ReviewSerializers(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ('watchlist',)


class WatchListSerializers(serializers.ModelSerializer):

    # reviews = ReviewSerializers(many=True, read_only=True)

    platform = serializers.CharField(source='platform.name')

    len_title = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
    @staticmethod
    def get_len_title(obj):
        return len(obj.title)


    # def validate_name(self, value):
    #     if len(value) < 2 :
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description should not be same")
    #     return data


class StreamPlatformSerializers(serializers.ModelSerializer):

    # watchlist = WatchListSerializers(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watchlist-details'
    )

    class Meta:
        model = StreamPlatform
        fields = '__all__'



