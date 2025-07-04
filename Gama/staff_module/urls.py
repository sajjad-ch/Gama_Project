from rest_framework import routers
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

router = routers.SimpleRouter()
urlpatterns = [
    path('collabrations/', csrf_exempt(CollabrationsViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }))),
    path('HR_need/', csrf_exempt(HumanRecourceNeedViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }))),
]

router.register(r'department', DepartmentViewSet)

urlpatterns += router.urls