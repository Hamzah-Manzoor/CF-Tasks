from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import index, events, leaves, profile, login, signup, like_lunch, dislike_lunch, like_dislike_status


urlpatterns = [
    path('', index, name='index'),
    path('events/', events, name='events'),
    path('leaves/', leaves, name='leaves'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('like/', like_lunch, name='like_lunch'),
    path('dislike/', dislike_lunch, name='dislike_lunch'),
    path('like-dislike-status/', like_dislike_status, name='like_dislike_status')
]

# urlpatterns = [
#     path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
#     path('employees/', EmployeeList.as_view(), name='employee-list'),
#     path('events/', EventList.as_view(), name='event-list'),
#     path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
# ]

# path('employees/<str:employee_id>/', views.get_employee_by_id, name='get_employee_by_id'),
# path('events/', views.get_events, name='get_events'),
# path('announcements/', views.get_announcements, name='get_announcements'),
