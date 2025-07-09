from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'collabrations', CollabrationsViewSet)
router.register(r'HR_need', HumanRecourceNeedViewSet)
router.register(r'job_title', JobTitleViewSet)

urlpatterns = router.urls