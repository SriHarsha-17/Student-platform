from django.urls import path
from courses.views.course_views import course_list, course_detail,CourseListCreateView

app_name = 'courses'
urlpatterns = [
    path('all',CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>',course_detail, name='course-detail')
]