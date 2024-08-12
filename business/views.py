from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

from datetime import date
from .models import TIME_EXISTENCE_CHOICES, STAGE_CHOICES, AREA_CHOICES
from .models import Company


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

    elif request.method == 'POST':
        business_name = request.POST.get('business_name')
        business_registration_number = request.POST.get('registration_number')
        business_website = request.POST.get('business_website')
        business_time_existence = request.POST.get('time_existence')
        business_description = request.POST.get('business_description')
        business_funding = request.POST.get('business_funding')
        business_percentage_return = request.POST.get('business_percentage_return')
        business_area = request.POST.get('area')
        business_target = request.POST.get('target')
        business_raise_expectation = request.POST.get('business_raise_expectation')
        business_stage = request.POST.get('business_stage')
        business_logo = request.FILES.get('business_logo')
        business_pitch = request.FILES.get('business_pitch')

        try:
            business = Company(
                name=business_name,
                company_number=business_registration_number,
                website=business_website,
                time_existence=business_time_existence,
                description=business_description,
                end_capture_date=business_funding,
                percent_equity=business_percentage_return,
                stage=business_stage,
                area=business_area,
                target_market=business_target,
                amount=business_raise_expectation,
                logo=business_logo,
                pitch=business_pitch,
                user=request.user
            )
            business.save()
            
        except Exception:
            messages.add_message(
                request,
                constants.ERROR,
                'An error occurred while saving your business. Please try again.'
            )

            return redirect(reverse('register_business'))
        
        messages.add_message(
            request,
            constants.SUCCESS,
            'Your business has been successfully saved.'
        )

        return redirect(reverse('list_businesses'))


@login_required(login_url='/users/signin/')
def list_businesses(request):
    if request.method == 'GET':
        companies = Company.objects.filter(user=request.user)
        context = {
            'companies': companies,
        }
        return render(
            request,
            'business/list_businesses.html',
            context=context
        )

def business_detail(request, id):
    if request.method == 'GET':
        company = Company.objects.get(id=id)
        return render(
            request,
            'business/business_detail.html',
            {
                'company': company
            }
        )
    else:
        return HttpResponse('Method not allowed', status=405)