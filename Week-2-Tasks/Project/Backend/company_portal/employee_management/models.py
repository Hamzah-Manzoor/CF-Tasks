from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    annual_leaves_taken = models.IntegerField(default=0)
    casual_leaves_taken = models.IntegerField(default=0)
    medical_leaves_taken = models.IntegerField(default=0)
    unpaid_leaves_taken = models.IntegerField(default=0)

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.name


class LeavesTaken(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_type = models.CharField(max_length=50)
    leave_taken_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'LeavesTaken'

    def __str__(self):
        return f'{self.employee_id.name} - {self.leave_type} from {self.start_date} to {self.end_date}'


class Events(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'Events'

    def __str__(self):
        return self.title


class Announcements(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    details = models.TextField()

    class Meta:
        db_table = 'Announcements'

    def __str__(self):
        return self.title

class LunchMenu(models.Model):
    dish_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'LunchMenu'

    def __str__(self):
        return self.dish_name


class AllocatedLeaves(models.Model):
    designation = models.CharField(max_length=255)
    annual_leaves = models.IntegerField()
    casual_leaves = models.IntegerField()
    medical_leaves = models.IntegerField()

    class Meta:
        db_table = 'AllocatedLeaves'

    def __str__(self):
        return self.designation


class Admin(models.Model):
    friday_lunch_iterator = models.IntegerField()
    weekday_lunch_iterator = models.IntegerField()
    lunch_time = models.TimeField(default="15:00:00")  # Assuming default lunch time

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return f'FridayIterator: {self.friday_lunch_iterator}, WeekdayIterator: {self.weekday_lunch_iterator}, LunchTime: {self.lunch_time}'


class LunchReview(models.Model):
    date = models.DateField(default=timezone.now)
    lunch_menu = models.ForeignKey(LunchMenu, on_delete=models.CASCADE)
    likes = models.JSONField(default=list, blank=True)
    dislikes = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'lunch_review'

    def __str__(self):
        return f'Date: {self.date}, Menu: {self.lunch_menu}, Likes: {len(self.likes)}, Dislikes: {len(self.dislikes)}'

