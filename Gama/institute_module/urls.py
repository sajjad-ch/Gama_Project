from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)
router.register(r'registeration', RegisteraionViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'comment_suggestion', CommentAndSuggestionViewSet)
router.register(r'headline_course', HeadlineCourseViewSet)
router.register(r'lessons_headline', LessonsHeadlineViewSet)

urlpatterns = [
    path('filter_active_course/', FilterActiveCourseView.as_view()),
    path('FilterRegisteringCourseView/', FilterRegisteringCourseView.as_view()),
    path('FilterCompletingRegisteringView/', FilterCompletingRegisteringView.as_view()),
    path('search-course/<str:course_name>/', SearchCourseView.as_view()),
    path('search-department/<str:department_name>/', SearchDepartmentCourseView.as_view()),
]

urlpatterns = router.urls
