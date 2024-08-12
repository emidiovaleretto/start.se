from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from datetime import date
from business.models import *


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    company_number = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    time_existence = models.CharField(max_length=2, choices=TIME_EXISTENCE_CHOICES, default="-6")
    description = models.TextField()
    end_capture_date = models.DateField()
    percent_equity = models.IntegerField()  # Percentage of equity offered
    stage = models.CharField(max_length=4, choices=STAGE_CHOICES, default='I')
    area = models.CharField(max_length=3, choices=AREA_CHOICES)
    target_market = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)  # Amount to be raised or sold
    pitch = models.FileField(upload_to='pitches')
    logo = models.FileField(upload_to='logos')

    def __str__(self):
        return f"{self.user.username} | {self.name}"

    @property
    def get_status(self):
        today = date.today()
        if today > self.end_capture_date:
            return mark_safe('<span class="bg-transparent border border-green-200 text-green-200 py-2 px-3 rounded-full text-xs font-bold">Completed</span>')
        return mark_safe('<span class="bg-transparent border border-yellow-200 text-yellow-200 py-2 px-3 rounded-full text-xs font-bold">In process</span>')
