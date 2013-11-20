__author__ = 'prashant'

from chartit import DataPool, Chart
from demoproject.utils.decorators import add_source_code_and_doc
from .models import MonthlyWeatherByCity, MonthlyWeatherSeattle, DailyWeather

#start_code
#pie chart for companies
    ds = DataPool(
           series=
            [{'options': {
                'source': CompanyWiseCarCount.objects.all()},
              'terms': [
                'CompanyName',
                'eleven']}
             ])

    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'CompanyName': [
                    'eleven']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Companies in USA'}},
            x_sortf_mapf_mts = (None, Companyname, False))
    #end_code
    #return render_to_response('chart_code.html', {'chart_list': cht,
    #                                         'code': code,
    #                                         'title': title,
    #                                         'doc': doc,
    #                                         'sidebar_items': sidebar_items})