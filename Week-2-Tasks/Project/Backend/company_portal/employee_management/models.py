from django.db import models

# Create your models here.

from django.db import models


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    total_annual_leaves = models.IntegerField(blank=True, null=True)
    leaves_taken = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.name


class Leaves(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'Leaves'

    def __str__(self):
        return f'{self.employee.name} - {self.leave_type} from {self.start_date} to {self.end_date}'


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

