from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class RegisteraionViewSet(viewsets.ModelViewSet):
    queryset = Registeration.objects.all()
    serializer_class = RegisterationSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAdminUser]


class CommentAndSuggestionViewSet(viewsets.ModelViewSet):
    queryset = CommentsAndSuggestions.objects.all()
    serializer_class = CommentsAndSuggestionsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]


class HeadlineCourseViewSet(viewsets.ModelViewSet):
    queryset = HeadlineCourse.objects.all()
    serializer_class = HeadlineCourseSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAdminUser]


class LessonsHeadlineViewSet(viewsets.ModelViewSet):
    queryset = LessonsHeadline.objects.all()
    serializer_class = LessonsHeadlineSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAdminUser]


class FilterActiveCourseView(APIView):
    def post(self, request):
        active_courses: Course = Course.objects.filter(is_active=True).all()
        if active_courses.DoesNotExist:
            return Response(message={'error': 'دوره فعالی یافت نشد.'}, status=status.HTTP_404_NOT_FOUND)
        paginator = LimitOffsetPagination()
        paginate_serializer = paginator.paginate_queryset(active_courses, request)
        serializer = CourseSerializer(paginate_serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FilterRegisteringCourseView(APIView):
    def post(self, request):
        registering_course: Course = Course.objects.filter(is_registering=True).all()
        if registering_course.DoesNotExist:
            return Response(message={'error': 'دوره در حال ثبت نامی یافت نشد.'}, status=status.HTTP_404_NOT_FOUND)
        paginator = LimitOffsetPagination()
        paginate_serializer = paginator.paginate_queryset(registering_course, request)
        serializer = CourseSerializer(paginate_serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterCompletingRegisteringView(APIView):
    def post(self, request):
        complete_registering_course: Course = Course.objects.filter(is_completing_registering=True).all()
        if complete_registering_course.DoesNotExist:
            return Response(message={'error': 'دوره ای به صورت تکمیل ظرفیت وجود ندارد.'})
        paginator = LimitOffsetPagination()
        paginate_serializer = paginator.paginate_queryset(complete_registering_course, request)
        serializer = CourseSerializer(paginate_serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SearchCourseView(APIView):
    def post(self, request, course_name):
        searched_course: Course = Course.objects.filter(course_name__icontains=course_name).all()
        if searched_course.DoesNotExist:
            return Response(message={'error': 'دوره ای با این نام یافت نشد.'}, status=status.HTTP_204_NO_CONTENT)
        paginator = LimitOffsetPagination()
        paginate_serializer = paginator.paginate_queryset(searched_course, request)
        serializer = CourseSerializer(paginate_serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SearchDepartmentCourseView(APIView):
    def post(self, request, department_name):
        department_course: Course = Course.objects.filter(course_department__department_name=department_name).all()
        if department_course.DoesNotExist:
            return Response(message={'error': f'دوره ای در دپارتمان {department_name} یافت نشد.'})
        paginator = LimitOffsetPagination()
        paginate_serializer = paginator.paginate_queryset(department_course, request)
        serializer = CourseSerializer(paginate_serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    