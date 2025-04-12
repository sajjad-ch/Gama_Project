from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)
router.register(r'registeration', RegisteraionViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'comment_suggestion', CommentAndSuggestionViewSet)

urlpatterns = router.urls
