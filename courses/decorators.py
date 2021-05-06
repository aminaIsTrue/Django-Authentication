
from .models import Course
from django.core.exceptions import PermissionDenied

def author_required(f):

    def wrap(request, id):

        obj = Course.objects.get(id = id)
        
        if  obj.author == request.user:

            return f(request, id)
        else:

            raise PermissionDenied
    
    return wrap