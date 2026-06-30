from django.urls import path
from courses.views.course_views import *
app_name = 'courses'
urlpatterns = [
    path('all',CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>',CourseDetailUpdateDeleteView.as_view(), name='course-detail')
]