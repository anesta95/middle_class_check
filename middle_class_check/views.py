from django.shortcuts import render
from django.http import HttpResponse
from .models import MedianHouseholdIncome
from .forms import AreaForm

# Create your views here.
def index(request):
    form = AreaForm()
    context = {'form': form}
    return render(request, 'index.html', context=context)

# def index(request):
#     """View function for home page of site."""
#     # Generate unique list of years, states, and area options
#     years = MedianHouseholdIncome.objects.values_list('year', flat=True).distinct().order_by('-year')
#     states = MedianHouseholdIncome.objects.exclude(state_name = 'United States').values_list('state_name', flat=True).distinct()
#     areas = MedianHouseholdIncome.objects.exclude(geography_name = 'national').values_list('geography_name', flat=True).distinct()
    
#     context = {
#         'unique_years': years,
#         'unique_states': states,
#         'unique_areas': areas,
#     }

#     # Render the HTML template index.html with the data in the context variable.
#     return render(request, 'index.html', context=context)

def locales(request):
    form = AreaForm(request.GET)
    return HttpResponse(form['geos'])
    # year = request.GET.get('year')
    # state_name = request.GET.get('state_name')
    # geography_name = request.GET.get('geography_name')
    # locales = MedianHouseholdIncome.objects.filter(year=year).filter(state_name=state_name).filter(geography_name=geography_name).distinct()
    # context = {'locales': locales}
    # return render(request, "partials/locales.html", context=context)