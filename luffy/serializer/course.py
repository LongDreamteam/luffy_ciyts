from luffy import models
from rest_framework import serializers
class CourseSerializer(serializers.ModelSerializer):
    """
    课程列表序列化
    """
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = models.Course
        fields = ['id','name','course_img','brief','level',]

class CourseDetailSerializers(serializers.ModelSerializer):
    """课程详细序列化"""
    name = serializers.CharField(source='course.name')
    course_img = serializers.CharField(source='course.course_img')
    brief = serializers.CharField(source='course.brief')
    level = serializers.CharField(source='course.get_level_display')
    recommend_courses = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    def get_recommend_courses(self,obj):
        """获取推荐课程"""
        queryset = obj.recommend_courses.all()
        return [{'id':i.id,'name':i.name} for i in queryset]
    def get_course(self,obj):
        """获取章节"""
        queryset = obj.course.coursechapters.all()
        return [{'id':i.id,'name':i.name} for i in queryset]

    class Meta:
        model = models.CourseDetail
        fields = ['id','name','brief','level','course_img','recommend_courses','course',]

