
import requests
from django.shortcuts import render

def get_covid_data(request):
    url = "https://corona.lmao.ninja/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()

    context = {
        'total_cases': data['cases'],
        'total_deaths': data['deaths'],
        'total_recovered': data['recovered'],
        'active_cases': data['active'],
        'critical_cases': data['critical'],
        'total_tests': data['tests'],
        'today_cases': data['todayCases'],
        'today_deaths': data['todayDeaths'],
        'updated_at': data['updated']
    }
    
    return render(request, 'tracker/index.html', context)
