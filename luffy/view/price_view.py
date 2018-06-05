from rest_framework.views import APIView
from rest_framework.response import Response
from luffy import models
from luffy.serializer.price import PricePolicyModelSerializer
class PricePolicyView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'status': False}
        try:
            course_id = kwargs.get('course_id')
            course_obj = models.Course.objects.get(pk=course_id)
            queryset = course_obj.price_policy.all()
            ser = PricePolicyModelSerializer(instance=queryset, many=True)
            response['data'] = ser.data
            response['status'] = True
        except Exception as e:
            response['error'] = str(e)
        return Response(response)
