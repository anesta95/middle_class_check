from django.shortcuts import render
from django.http import HttpResponse
from .models import MedianHouseholdIncome
from .forms import AreaForm
from .plotly_plot import *

# Create your views here.
def index(request):
    form = AreaForm()
    context = {'form': form}
    return render(request, 'index.html', context=context)

def locales(request):
    form = AreaForm(request.GET)
    return HttpResponse(form['geoid'])

def results(request):
    year = request.GET.get('year')
    state_name = request.GET.get('state')
    geography_name = request.GET.get('area')
    geoid = request.GET.get('geoid')
    provided_income = int(request.GET.get('income'))

    area_income = int(MedianHouseholdIncome.objects.filter(year=year).filter(geoid=geoid).values_list('median_hh_income', flat=True)[0])
    national_income = int(MedianHouseholdIncome.objects.filter(year=year).filter(geoid='1').values_list('median_hh_income', flat=True)[0])
    area_moe = int(MedianHouseholdIncome.objects.filter(year=year).filter(geoid=geoid).values_list('moe', flat=True)[0])
    national_moe = int(MedianHouseholdIncome.objects.filter(year=year).filter(geoid='1').values_list('moe', flat=True)[0])
    area_name = str(MedianHouseholdIncome.objects.filter(year=year).filter(geoid=geoid).values_list('name', flat=True)[0])

    area_income_diff = round(((provided_income / area_income) - 1) * 100, 1)
    national_income_diff = round(((provided_income / national_income) - 1) * 100, 1)

    area_income_direction = 'more' if provided_income > area_income else 'less'
    national_income_direction = 'more' if provided_income > national_income else 'less'
    text_res = f'''
    According to data from the <a href="https://www.census.gov/programs-surveys/acs" target="_blank">U.S. Census Bureau</a>, in {year} your household made {str(area_income_diff)}% {area_income_direction} 
    than the median household in {area_name}, and  {str(national_income_diff)}% 
    {national_income_direction} than the median household in the United States.
    '''

    bar_chart = plotly_plot(year, provided_income, area_income, national_income, area_name, area_moe, national_moe)

    context = {
        'text_res': text_res,
        'bar_chart': bar_chart
    }

    return render(request, 'results.html', context=context)





    