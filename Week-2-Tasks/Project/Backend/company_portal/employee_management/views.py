# from django.http import JsonResponse
# from .models import Employees, Events, Announcements
# from rest_framework.generics import RetrieveAPIView, ListAPIView
# from .serializers import EmployeeSerializer, EventSerializer, AnnouncementSerializer
#
#
# class EmployeeDetail(RetrieveAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EmployeeList(ListAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EventList(ListAPIView):
#     queryset = Events.objects.all()
#     serializer_class = EventSerializer
#
#
# class AnnouncementList(ListAPIView):
#     queryset = Announcements.objects.all()
#     serializer_class = AnnouncementSerializer
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Employees, Events, Announcements, LunchMenu, AllocatedLeaves, LeavesTaken, Admin, LunchReview
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt

import logging

logger = logging.getLogger(__name__)


def index(request):
    employees = Employees.objects.all()

    # Filter events: the two closest to present time in the future
    upcoming_events = Events.objects.filter(date__gt=timezone.now()).order_by('date')[:2]
    #upcoming_events = Events.objects.all()

    # Filter announcements: the two nearest from the past according to present time
    recent_announcements = Announcements.objects.filter(date__lt=timezone.now()).order_by('-date')[:2]

    # For Leaves
    employee_id = 1  # Change this to the specific employee ID you want to fetch
    employees_leaves = Employees.objects.get(id=employee_id)
    allocated_leaves = AllocatedLeaves.objects.get(designation=employees_leaves.position)

    # For Birthdays
    today = date.today()
    future_date = today + timedelta(days=150)

    upcoming_birthdays = []
    for employee in employees:
        birthdate_this_year = employee.birthdate.replace(year=today.year)
        if birthdate_this_year < today:
            birthdate_this_year = birthdate_this_year.replace(year=today.year + 1)

        if today <= birthdate_this_year <= future_date:
            upcoming_birthdays.append(employee)

    # Sort the upcoming birthdays
    upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: x.birthdate.replace(year=today.year))[:5]














    admin = Admin.objects.first()

    # Starting date
    start_date = datetime.strptime('2024-07-01', '%Y-%m-%d').date()

    # Current date
    today = datetime.today().date()

    # Number of days since the start date
    days_since_start = (today - start_date).days

    # Number of weekdays since the start date (excluding weekends)
    weekdays_since_start = sum(1 for day in range(days_since_start + 1)
                               if (start_date + timedelta(days=day)).weekday() < 5)

    # Calculate the number of Fridays since the start date
    fridays_since_start = sum(1 for day in range(days_since_start + 1)
                              if (start_date + timedelta(days=day)).weekday() == 4)

    weekdays_since_start -= fridays_since_start

    if weekdays_since_start % 15:
        weekday_lunch_iterator = (weekdays_since_start % 15) + 2  # Range from 3 to 17
    else:
        weekday_lunch_iterator = 17
    if fridays_since_start % 2:
        friday_lunch_iterator = (fridays_since_start % 2)  # Range between 1 and 2
    else:
        friday_lunch_iterator = 2

    day_of_week = today.weekday()
    if day_of_week == 4:  # Friday
        menu_item = LunchMenu.objects.all()[friday_lunch_iterator - 1]
    elif day_of_week < 4:  # Monday to Thursday
        menu_item = LunchMenu.objects.all()[weekday_lunch_iterator - 1]
    else:
        menu_item = "Off-Day"  # For Saturday and Sunday


    # Print the values to the terminal
    # print(f"todays date is: {datetime.today()}")
    # print(f"todays date is: {today}")
    # print(f"days_since_start: {days_since_start}")
    # print(f"weekdays_since_start: {weekdays_since_start}")
    # print(f"fridays_since_start: {fridays_since_start}")
    # print(f"weekday_lunch_iterator: {weekday_lunch_iterator}")
    # print(f"friday_lunch_iterator: {friday_lunch_iterator}")






    # Handle LunchReview for today
    lunch_review, created = LunchReview.objects.get_or_create(
        date=today,
        defaults={'lunch_menu': menu_item}
    )












    context = {
        'employees': employees,
        'events': upcoming_events,
        'announcements': recent_announcements,
        'upcoming_birthdays': upcoming_birthdays,
        'allocated_leaves': allocated_leaves,
        # For Lunch Card
        'admin': admin,
        'todays_menu': menu_item,
        'likes_count': len(lunch_review.likes),
        'dislikes_count': len(lunch_review.dislikes),
    }

    return render(request, 'index.html', context)


# @login_required
@csrf_exempt
def like_lunch(request):
    print("You are in like_lunch function")

    today = date.today()
    lunch_review = get_object_or_404(LunchReview, date=today)

    user_id = 1  # request.user.id
    if user_id in lunch_review.likes:
        lunch_review.likes.remove(user_id)
    else:
        lunch_review.likes.append(user_id)
        if user_id in lunch_review.dislikes:
            lunch_review.dislikes.remove(user_id)

    lunch_review.save()

    return JsonResponse({'likes_count': len(lunch_review.likes), 'dislikes_count': len(lunch_review.dislikes)})


# @login_required
@csrf_exempt
def dislike_lunch(request):
    today = date.today()
    lunch_review = get_object_or_404(LunchReview, date=today)

    user_id = 1  # request.user.id
    if user_id in lunch_review.dislikes:
        lunch_review.dislikes.remove(user_id)
    else:
        lunch_review.dislikes.append(user_id)
        if user_id in lunch_review.likes:
            lunch_review.likes.remove(user_id)

    lunch_review.save()

    return JsonResponse({'likes_count': len(lunch_review.likes), 'dislikes_count': len(lunch_review.dislikes)})


# @login_required
def like_dislike_status(request):
    today = date.today()
    lunch_review = LunchReview.objects.filter(date=today).first()

    user_id = 1  # request.user.id
    liked = False
    disliked = False

    if lunch_review:
        liked = user_id in lunch_review.likes
        disliked = user_id in lunch_review.dislikes

    return JsonResponse({'liked': liked, 'disliked': disliked})


def events(request):
    # upcoming_events = Events.objects.filter(date__gte=timezone.now()).order_by('date')
    # recent_announcements = Announcements.objects.filter(date__lte=timezone.now()).order_by('-date')

    upcoming_events = Events.objects.all().order_by('date')
    recent_announcements = Announcements.objects.all().order_by('-date')

    context = {
        'upcoming_events': upcoming_events,
        'recent_announcements': recent_announcements
    }

    return render(request, 'events.html', context)


def leaves(request):
    employee_id = 1  # Change this to the specific employee ID you want to fetch
    employee = Employees.objects.get(id=employee_id)
    allocated_leaves = get_object_or_404(AllocatedLeaves, designation=employee.position)

    if request.method == 'POST':
        leave_type = request.POST.get('leave-type')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        reason = request.POST.get('reason')

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            leave_days = (end_date - start_date).days + 1

            if leave_type == 'Annual Leave':
                if employee.annual_leaves_taken + leave_days > allocated_leaves.annual_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.annual_leaves_taken} annual leaves. You can take a maximum of {allocated_leaves.annual_leaves - employee.annual_leaves_taken} more annual leaves.'
                    }, status=400)
                employee.annual_leaves_taken += leave_days

            elif leave_type == 'Medical Leave':
                if employee.medical_leaves_taken + leave_days > allocated_leaves.medical_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.medical_leaves_taken} medical leaves. You can take a maximum of {allocated_leaves.medical_leaves - employee.medical_leaves_taken} more medical leaves.'
                    }, status=400)
                employee.medical_leaves_taken += leave_days

            elif leave_type == 'Casual Leave':
                if employee.casual_leaves_taken + leave_days > allocated_leaves.casual_leaves:
                    return JsonResponse({
                        'error': f'You have already taken {employee.casual_leaves_taken} casual leaves. You can take a maximum of {allocated_leaves.casual_leaves - employee.casual_leaves_taken} more casual leaves.'
                    }, status=400)
                employee.casual_leaves_taken += leave_days

            elif leave_type == 'Unpaid Leave':
                employee.unpaid_leaves_taken += leave_days

            employee.save()

            # Add entry to LeavesTaken
            LeavesTaken.objects.create(
                employee_id=employee,
                start_date=start_date,
                end_date=end_date,
                reason=reason,
                leave_type=leave_type,
                leave_taken_count=leave_days
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    context = {
        'employee': employee,
        'allocated_leaves': allocated_leaves,
    }

    return render(request, 'leaves.html', context)


def profile(request):
    return render(request, 'profile.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
