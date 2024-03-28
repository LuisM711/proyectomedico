from django.utils.deprecation import MiddlewareMixin

class UserTypeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_type = request.session.get('user_type')
        request.user_type = user_type
