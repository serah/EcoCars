# Create your views here.
from django.template import RequestContext
import twython
from django.shortcuts import render_to_response

TWITTER_APP_KEY = 'F0kcD4RLRQSTAyOIXlgTbg'
TWITTER_APP_KEY_SECRET = '5cztY0PmgmgYZ8qdmDZGyUc4VbzsnQOTa1b34nqdg'
TWITTER_ACCESS_TOKEN = '2196719624-0iS9ewgAFSSfBkiVGh5okUcKMaThUQ1Ymw14OUE'
TWITTER_ACCESS_TOKEN_SECRET = 'WfNby6swgDCMQaCtm8cMvV0RQ9vwt6LTQBNtmaN8xf6oR'

def home(request):
    #t = twython.Twython(app_key=TWITTER_APP_KEY,
    #                    app_secret=TWITTER_APP_KEY_SECRET,
    #                    oauth_token=TWITTER_ACCESS_TOKEN,
    #                    oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
    #
    #search = t.search(q='#electriccars', count=1)
    #search2 = t.search(q="#gasoline", count=1)
    #
    #tweets = search['statuses']
    #tweets += search2['statuses']
    #tweet_list = {}
    #
    #for tweet in tweets:
    #    print 'in dictionary loop:::::::'
    #    tweet_list[tweet['text']] = tweet['user']['screen_name']
    #for t in tweet_list:
    #    print t, "::", tweet_list[t], '\n'
    tweet = {}
    return render_to_response('home.html', {'context_instance':tweet})
