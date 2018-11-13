from django.urls import include, path
from django.conf.urls import  url
from . import views

from rest_framework import routers

# from .view.course.viewsets import CourseCategoryCreateView, CourseCategoryDetailView, SubjectDetailUpdateAPIView, SubjectListCreateAPIView, ClassDetailUpdateAPIView, ClassListCreateAPIView

from .view.course import (
    base_views as course_base_views,
)
from .view.syllabus import (
    base_views as syllabus_base_views,
)
from .view.user import (
    base_views as user_base_views,
)

# from .view.course import CourseCategoryDeleteView,CourseCayegoryUpdateView,CourseCategoryDetailView,CourseCategoryListView,CourseCategoryCreateView

from .view.course import  viewsets

app_name = "api"

router = routers.SimpleRouter()
# router.register(r'courses', CourseCategoryListCreateAPIView, base_name="Courses")
# router.register(r'courses', CourseCategoryDetailUpdateAPIView, base_name="Courses")
# router.register(r'subjects', SubjectDetailUpdateAPIView, base_name="Subjects")
# router.register(r'subjects', SubjectListCreateAPIView, base_name="Subjects")
# router.register(r'classes', ClassDetailUpdateAPIView, base_name="Subjects")
# router.register(r'classes', ClassListCreateAPIView, base_name="Subjects")

course_category_urlpatterns = [
    path('create', viewsets.CourseCategoryCreateView.as_view(), name="course_category_create"),
    path('list', viewsets.CourseCategoryListView.as_view(), name="course_category_list"),
    path('detail/<int:id>/', viewsets.CourseCategoryDetailView.as_view(), name="course_category_detail"),
    path('update/<int:id>/', viewsets.CourseCayegoryUpdateView.as_view(), name="course_category_update"),
    path('delete/<int:id>/', viewsets.CourseCategoryDeleteView.as_view(), name="course_category_delete"),
]

subject_urlpatterns = [
    path('create', viewsets.SubjectCreateView.as_view(), name="subject_create"),
    path('list', viewsets.SubjectListView.as_view(), name="subject_list"),
    path('detail/<int:id>/', viewsets.SubjectDetailView.as_view(), name="subject_detail"),
    path('update/<int:id>/', viewsets.SubjectUpdateView.as_view(), name="subject_update"),
    path('delete/<int:id>/', viewsets.SubjectDeleteView.as_view(), name="subject_delete"),
]

class_urlpatterns = [
    path('create', viewsets.ClassCreateView.as_view(), name="class_create"),
    path('list', viewsets.ClassListView.as_view(), name="class_list"),
    path('detail/<int:id>/', viewsets.ClassDetailView.as_view(), name="class_detail"),
    path('update/<int:id>/', viewsets.ClassUpdateView.as_view(), name="class_update"),
    path('delete/<int:id>/', viewsets.ClassDeleteView.as_view(), name="class_delete"),
]

class_lecturer_urlpatterns = [
    path('create', viewsets.ClassLecturerCreateView.as_view(), name="class_lecturer_create"),
    path('list', viewsets.ClassLecturerListView.as_view(), name="class_lecturer_list"),
    path('detail/<int:id>/', viewsets.ClassLecturerDetailView.as_view(), name="class_lecturer_detail"),
    path('update/<int:id>/', viewsets.ClassLecturerUpdateView.as_view(), name="class_lecturer_update"),
    path('delete/<int:id>/', viewsets.ClassLecturerDeleteView.as_view(), name="class_lecturer_delete"),
]

class_student_urlpatterns = [
    path('create', viewsets.ClassStudentCreateView.as_view(), name="class_student_create"),
    path('list', viewsets.ClassStudentListView.as_view(), name="class_student_list"),
    path('detail/<int:id>/', viewsets.ClassStudentDetailView.as_view(), name="class_student_detail"),
    path('update/<int:id>/', viewsets.ClassStudentUpdateView.as_view(), name="class_student_update"),
    path('delete/<int:id>/', viewsets.ClassStudentDeleteView.as_view(), name="class_student_delete"),
]

enroll_request_urlpatterns = [
    path('create', viewsets.ClassCreateView.as_view(), name="class_create"),
    path('list', viewsets.ClassListView.as_view(), name="class_list"),
    path('detail/<int:id>/', viewsets.ClassDetailView.as_view(), name="class_detail"),
    path('update/<int:id>/', viewsets.ClassUpdateView.as_view(), name="class_update"),
    path('delete/<int:id>/', viewsets.ClassDeleteView.as_view(), name="class_delete"),
]

schedule_urlpatterns = [
    path('create', viewsets.ScheduleCreateView.as_view(), name="schedule_create"),
    path('list', viewsets.ScheduleListView.as_view(), name="schedule_list"),
    path('detail/<int:id>/', viewsets.ScheduleDetailView.as_view(), name="schedule_detail"),
    path('update/<int:id>/', viewsets.ScheduleUpdateView.as_view(), name="schedule_update"),
    path('delete/<int:id>/', viewsets.ScheduleDeleteView.as_view(), name="schedule_delete"),
]


course_url_patterns= [
    # path('',course_base_views._Course.as_view()),
    path('course_info', course_base_views.GetCourses.as_view()),
    # path('class_info',course_base_views._Class.as_view()),
]

syllabus_url_patterns= []

user_url_patterns=[]

urlpatterns = [
    path('auth',views.login, name="login"),
    path('course/',include(course_url_patterns)),
    path('syllabus/',include(syllabus_url_patterns)),
    path('user/',include(user_url_patterns)),
    # path('', include(router.urls)),
    path('course_category/', include(course_category_urlpatterns)),
    path('subject/', include(subject_urlpatterns)),
    path('class/', include(class_urlpatterns)),
    path('class-lecturer/', include(class_lecturer_urlpatterns)),
    path('class-student/', include(class_student_urlpatterns)),
    path('enroll_request/', include(enroll_request_urlpatterns)),
    path('schedule/', include(schedule_urlpatterns)),

]