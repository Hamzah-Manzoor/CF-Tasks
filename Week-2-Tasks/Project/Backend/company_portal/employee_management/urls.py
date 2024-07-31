from django.urls import path
# from .views import EmployeeDetail, EmployeeList, EventList, AnnouncementList
from .views import index, events, leaves, profile, login, signup, like_lunch, logout
# from .views import user_list  # user_detail, user_edit, user_delete, user_create
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('events/', events, name='events'),
    path('leaves/', leaves, name='leaves'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('like_lunch/', like_lunch, name='like_lunch'),
    # path('dislike_lunch/', dislike_lunch, name='dislike_lunch'),
    # path('like-dislike-status/', like_dislike_status, name='like_dislike_status'),
    path('logout/', logout, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.users_create, name='users_create'),
    path('users/delete/<int:id>/', views.users_delete, name='users_delete'),
    # path('users/<int:id>/', views.user_detail, name='user_detail'),
    path('users/update/', views.user_update, name='user_update'),
    # path('users/edit/<int:id>/', views.user_edit, name='user_edit'),

    path('events/create/', views.event_create, name='event_create'),
    path('events/edit/<int:event_id>/', views.event_edit, name='event_edit'),
    path('events/delete/<int:event_id>/', views.event_delete, name='event_delete'),

    path('manage_leaves/', views.manage_leaves, name='manage_leaves'),
    path('leaves/create/', views.create_leave, name='leave_create'),
    path('leaves/update/', views.update_leave, name='leave_update'),
    path('leaves/delete/<int:leave_id>/', views.delete_leave, name='leave_delete'),
    path('leave_approve_reject/<int:leave_id>/', views.leave_approve_reject, name='leave_approve_reject'),

    path('manage_lunch_menu/', views.manage_lunch_menu, name='manage_lunch_menu'),
    path('manage_lunch_menu/update_admin/', views.update_admin, name='admin_update'),
    path('manage_lunch_menu/create/', views.lunch_menu_create, name='lunch_menu_create'),
    path('manage_lunch_menu/update/', views.update_lunch_menu, name='lunch_menu_update'),
    path('manage_lunch_menu/delete/', views.delete_lunch_menu, name='lunch_menu_delete'),

    path('projects/', views.manage_projects, name='manage_projects'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),

    path('feedback/', views.manage_feedback, name='manage_feedback'),
    path('feedback/add/', views.add_feedback, name='add_feedback'),
    path('feedback/edit/<int:feedback_id>/', views.edit_feedback, name='edit_feedback'),
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),

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
