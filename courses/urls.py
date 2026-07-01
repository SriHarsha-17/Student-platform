from django.urls import path
from courses.views.course_views import *
from courses.views.exam_views import *
app_name = 'courses'
urlpatterns = [
    # courses patterms
    path('all',CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>',CourseDetailUpdateDeleteView.as_view(), name='course-detail'),


    # exams patterns
    path('exam/all',ExamCreateListView.as_view(), name='exam-list'),
    path('exam/<slug:pk>', ExamDetailUpdateDeleteView.as_view(), name='exam-detail')
]