# -*- coding: utf-8 -*-

from models import Article, CmdbCi, CmdbCiIp
from rest_framework import serializers


# Serializers定义了API的表现.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url', 'title', 'content', 'pub_time')
