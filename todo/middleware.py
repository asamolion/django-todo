from datetime import datetime

class UserTimeMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def process_request(self, request):
        print('hello ')
        return None

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        with open('userlog.txt', 'a') as f:
            f.write('User: %s | Time: %s\n' % (
                request.user, datetime.now()
            ))
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response
