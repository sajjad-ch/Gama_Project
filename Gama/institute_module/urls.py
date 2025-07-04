from django.urls import path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

from .views import *

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)
router.register(r'registeration', RegisteraionViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'headline_course', HeadlineCourseViewSet)
router.register(r'lessons_headline', LessonsHeadlineViewSet)
router.register(r'institue_data', InstitueDataViewSet)

urlpatterns = [
    path('filter_active_course/', FilterActiveCourseView.as_view(), name='active-course'),
    path('filter_registering_course/', FilterRegisteringCourseView.as_view(), name='registering-course'),
    path('filter_completing_registering/', FilterCompletingRegisteringView.as_view(), name='completeing-registering'),
    path('search-course/<str:course_name>/', SearchCourseView.as_view(), name='search-course'),
    path('search-department/<str:department_name>/', SearchDepartmentCourseView.as_view(), name='search-department'),
]

urlpatterns += [
    path('comment_suggestion/', csrf_exempt(CommentAndSuggestionViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }))),
]

urlpatterns += router.urls
