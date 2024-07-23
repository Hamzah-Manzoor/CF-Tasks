from django.http import JsonResponse
from .models import Employees, Events, Announcements
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import EmployeeSerializer, EventSerializer, AnnouncementSerializer


class EmployeeDetail(RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EventList(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class AnnouncementList(ListAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer
