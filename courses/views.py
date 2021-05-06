from django.shortcuts import render, redirect
from .models import Course
from .forms import CreateCourseForm
from.decorators import author_required

# Create your views here.

def course_list(request):


    return render (request, 'courses/course-list.html', {'courses' : Course.objects.all()})


def course_detail(request, pk):


    return render (request, 'courses/course-detail.html', {'course' : Course.objects.get(id = pk)})


# create a new course using django forms

def create_course(request):

    if request.method == 'POST':
        obj = CreateCourseForm(request.POST, request.FILES)
        #print ('#####################  before valid ###############  ' , obj.image.url )
        if obj.is_valid():
            obj = obj.save(commit = False)
            obj.author = request.user
            obj.save()
            return redirect('course-home-path')

    return render(request,'courses/create-course.html', {'form' : CreateCourseForm()})



@author_required
def update_course(request, id):
    # obj = Course.objects.get(id = id) 
    # if obj.author ==  request.user:
    if request.method == 'POST':
        obj = CreateCourseForm(request.POST, request.FILES, instance = Course.objects.get(id = id))
        
        if obj.is_valid():
            obj = obj.save(commit = False)
            obj.author = request.user
            obj.save()
            return redirect('course-home-path')

    # else:
    #     raise PermissionDenied
    return render(request,'courses/update-course.html', {'form' : CreateCourseForm(instance = Course.objects.get(id = id)),
                                                            'course' : Course.objects.get(id = id) })

@author_required
def delete_course(request, id):
    # obj = Course.objects.get(id = id) 
    # if obj.author ==  request.user:

    obj = Course.objects.get(id = id)

    if request.method == 'POST':       
        obj.delete()
        return redirect('course-home-path')

    # else:
    #     raise PermissionDenied
    return render(request,'courses/delete-course.html')