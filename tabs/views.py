# Create your views here.
import twython
from django.shortcuts import render_to_response
from chartit import DataPool, Chart
from tabs.models import CompanyWiseCarCount

TWITTER_APP_KEY = 'F0kcD4RLRQSTAyOIXlgTbg'
TWITTER_APP_KEY_SECRET = '5cztY0PmgmgYZ8qdmDZGyUc4VbzsnQOTa1b34nqdg'
TWITTER_ACCESS_TOKEN = '2196719624-0iS9ewgAFSSfBkiVGh5okUcKMaThUQ1Ymw14OUE'
TWITTER_ACCESS_TOKEN_SECRET = 'WfNby6swgDCMQaCtm8cMvV0RQ9vwt6LTQBNtmaN8xf6oR'


def home(request):
    return render_to_response('home.html')


def count(request):
    ds = DataPool(
        series=
        [{'options': {
            'source': CompanyWiseCarCount.objects.all()},
          'terms': [
              'CompanyName',
              'eleven']}
        ])
    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'pie',
            'stacking': False},
          'terms': {
              'CompanyName': [
                  'eleven']
          }}],
        chart_options=
        {'title': {
            'text': 'Weather Data of Boston and Houston'}, })

    return render_to_response('count.html', {'cht': cht})

def advantages(request):
    return render_to_response('advantages.html')

def companies(request):
    return render_to_response('companies.html')

def mileage(request):
    return render_to_response('mileage.html')

def demand(request):
    return render_to_response('demand.html')

def saved(request):
    return render_to_response('saved.html')

def sources(request):
    return render_to_response('sources.html')

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
    return render_to_response('calculator.html')
