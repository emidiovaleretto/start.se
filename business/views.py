from django.shortcuts import render
from .models import TIME_EXISTENCE_CHOICES, STAGE_CHOICES, AREA_CHOICES
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/signin/')
def register_business(request):
    if request.method == 'GET':
        return render(
            request,
            'business/register_business.html',
            {
                'time_existence_choices': TIME_EXISTENCE_CHOICES,
                'stage_choices': STAGE_CHOICES,
                'area_choices': AREA_CHOICES
            })
