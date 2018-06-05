
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from rest_framework.views import APIView
from luffy import models
from luffy.serializer.course import CourseSerializer
from luffy.serializer.course import CourseDetailSerializers

class CourseView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程列表接口
        """
        ret = {'code':1000,'data':None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """课程详情"""
        ret = {'code':1000,'data':None}
        try:
            pk = kwargs.get("pk")
            courseDetail_q = models.CourseDetail.objects.filter(course_id=pk).first()
            set = CourseDetailSerializers(instance=courseDetail_q,many=False)
            ret['data'] = set.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取课程详细失败！"
        return Response(ret)

