from luffy import models
from rest_framework import serializers


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'head_img', 'comment_num', 'brief', 'agree_num', 'view_num','content','source','date','collect_num']


class ArticleDetailModelSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'source', 'article_type', 'head_img', 'content', 'status', 'vid', 'comment_num',
                  'agree_num', 'view_num', 'collect_num']
