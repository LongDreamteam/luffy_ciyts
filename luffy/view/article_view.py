from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin,ModelViewSet
from rest_framework.response import Response
from luffy import models
from luffy.serializer.article import ArticleModelSerializer

class ArticleView(ViewSetMixin, APIView):
    """
    深科技
    """
    def get(self, request, *args, **kwargs):
        ret = {'code':1000}
        try:
            articles = models.Article.objects.all()
            ser = ArticleModelSerializer(instance=articles, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['error'] = str(e)
        return Response(ret)


    def retrieve(self, request,*args,**kwargs):
        ret = {'code':1000,'data':None}
        try:
            pk = kwargs.get("pk")
            print(pk)
            article_obj = models.Article.objects.filter(id=pk).first()
            ser = ArticleModelSerializer(instance=article_obj, many=False)
            print("////////////////////////// /////////////////////////////////")
            ret['data'] = ser.data
            ret['status'] = True
        except Exception as e:
            ret['error'] = str(e)
        return Response(ret)
