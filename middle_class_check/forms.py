from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin
from .models import MedianHouseholdIncome

class AreaForm(DynamicFormMixin, forms.Form):

    def geo_choices(form):
        year = form['year'].value()
        state_name = form['state'].value()
        geography_name = form['area'].value()
        return MedianHouseholdIncome.objects.filter(year=year).filter(state_name=state_name).filter(geography_name=geography_name).distinct()

    def initial_geo(form):
        year = form['year'].value()
        state_name = form['state'].value()
        geography_name = form['area'].value()
        return MedianHouseholdIncome.objects.filter(year=year).filter(state_name=state_name).filter(geography_name=geography_name).distinct().first()

    # Year field
    year = forms.ModelChoiceField(
        queryset=MedianHouseholdIncome.objects.values_list('year', flat=True).distinct().order_by('-year'),
        initial=MedianHouseholdIncome.objects.values_list('year', flat=True).distinct().order_by('-year').first()
    )

    # State field
    state = forms.ModelChoiceField(
        queryset=MedianHouseholdIncome.objects.exclude(state_name = 'United States').values_list('state_name', flat=True).distinct(),
        initial=MedianHouseholdIncome.objects.exclude(state_name = 'United States').values_list('state_name', flat=True).distinct().first()
    )

    # Areas field
    area = forms.ModelChoiceField(
        queryset=MedianHouseholdIncome.objects.exclude(geography_name = 'national').values_list('geography_name', flat=True).distinct(),
        initial=MedianHouseholdIncome.objects.exclude(geography_name = 'national').values_list('geography_name', flat=True).distinct().first()
    )

    # Geo dynamic field
    geoid = DynamicField(
        forms.ModelChoiceField,
        queryset=geo_choices,
        initial=initial_geo,
        to_field_name="geoid"
    )

    income = forms.IntegerField(
        min_value = 0,
        max_value = 100000000
    )