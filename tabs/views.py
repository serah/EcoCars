# Create your views here.
import twython
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from chartit import DataPool, Chart
from tabs.models import CompanyWiseCarCount, GasRate, CarCount, Mileage, GasolineCarCount, GrowthPerYear, ElectricitySources
from tabs.forms import Save

TWITTER_APP_KEY = 'F0kcD4RLRQSTAyOIXlgTbg'
TWITTER_APP_KEY_SECRET = '5cztY0PmgmgYZ8qdmDZGyUc4VbzsnQOTa1b34nqdg'
TWITTER_ACCESS_TOKEN = '2196719624-0iS9ewgAFSSfBkiVGh5okUcKMaThUQ1Ymw14OUE'
TWITTER_ACCESS_TOKEN_SECRET = 'WfNby6swgDCMQaCtm8cMvV0RQ9vwt6LTQBNtmaN8xf6oR'


def home(request):
    return render_to_response('home.html')


def count(request):
    electric = CarCount.objects.filter()
    gas = GasolineCarCount.objects.filter()
    growth = GrowthPerYear.objects.filter()
    return render_to_response('count.html', {'electric': electric, 'gas': gas, 'growth': growth})

def advantages(request):
    return render_to_response('advantages.html')

def references(request):
    return render_to_response('references.html')

def companies(request):
    companies = CompanyWiseCarCount.objects.filter()
    return render_to_response('companies.html', {'company_data': companies})

def mileage(request):
    return render_to_response('mileage.html')

def demand(request):
    return render_to_response('demand.html')

def saved(request):
    return render_to_response('saved.html')

def sources(request):
    sources = ElectricitySources.objects.filter()
    return render_to_response('sources.html', {'sources': sources})

def about(request):
    return render_to_response('about.html')

def stations(request):
    return render_to_response('stations.html')


def twitter(request):
    t = twython.Twython(app_key=TWITTER_APP_KEY,
                        app_secret=TWITTER_APP_KEY_SECRET,
                        oauth_token=TWITTER_ACCESS_TOKEN,
                        oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    search = t.search(q='#electriccars', count = 30)
    search2 = t.search(q="#gasoline", count = 30)

    tweets = search['statuses']
    tweets += search2['statuses']
    tweet_list = {}

    for tweet in tweets:
        tweet_list[tweet['text']] = tweet['user']['screen_name']

    return render_to_response('twitter.html', {'tweets': tweet_list})

def calculator(request):
    state_db = GasRate.objects.values('state')
    states = []
    for s in state_db:
        states.append(s['state'])
    form = Save()
    if request.method == 'POST':
        form = Save(request.POST)
        if form.is_valid():
            form_state = form.cleaned_data['state']
            miles = form.cleaned_data['miles']
            cartype = form.cleaned_data['cartype']
            print form_state,miles,cartype
            for s in states:
                if s == form_state:
                    price_obj = GasRate.objects.raw("select id,price from tabs_gasrate where state = 'Texas';")
            for p in price_obj:
                price = p.price

            cost = (float(miles)/float(cartype)) * price * 4 * 12
            electric_cost = 0.04 * miles * 4 *12
            savings = cost - electric_cost
            return render_to_response('calculated.html',{'saving':savings})
        else:
            return render_to_response('calculator.html',{'states':states,'form':form}, context_instance = RequestContext(request))

    return render(request, 'calculator.html', {'states':states,'form':form})
