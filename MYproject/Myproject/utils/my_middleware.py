from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection
class Cors_middleware(MiddlewareMixin):
    def process_response(self,request,response):
        response["Access-Control-Allow-Origin"]="*"
        response['Access-Control-Allow-Headers'] = ["Content-Type","headers"]  # 其他的编码方式比如 json
        response['Access-Control-Allow-Methods'] = "DELETE,PUT,POST"
        print(">走了这部>>")
        return response

class Redis_middleware(MiddlewareMixin):
    dl=None
    def process_request(self,request):
        if self.dl:
            request.conn=self.dl
        else :
            conn = get_redis_connection()
            self.dl=conn
            request.conn = conn


