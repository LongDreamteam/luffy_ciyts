from rest_framework.views import APIView
from rest_framework.response import Response
from luffy import models
import uuid
class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000}
        user = request.data.get('username')
        pwd = request.data.get('password')
        print(user,pwd)
        user = models.Account.objects.filter(username=user,password=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=user,defaults={'token':uid})
            ret['token'] = uid
        return Response(ret)