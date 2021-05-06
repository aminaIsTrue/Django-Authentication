import django_filters

from .models import Course

class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label = 'search by title' ,lookup_expr='icontains')
    content = django_filters.CharFilter(label = 'search by content' ,lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['title', 'content']