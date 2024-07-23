from django.urls import path
from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList

urlpatterns = [
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('events/', EventList.as_view(), name='event-list'),
    path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
]
# path('employees/<str:employee_id>/', views.get_employee_by_id, name='get_employee_by_id'),
# path('events/', views.get_events, name='get_events'),
# path('announcements/', views.get_announcements, name='get_announcements'),
