from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ..model.serializers import SearchHistorySerializer, TweetSerializer
from ..model.models import SearchHistory, Tweet

import tweepy

from rest_framework import viewsets, generics


def index(request):
    return render(request, 'tweetapp/index.html')


def history(request):
    hist = SearchHistory.objects.all()
    return render(request, 'tweetapp/history.html', {'history': hist})


class SearchHistoryAPIView(viewsets.ModelViewSet):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer


class SearchAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TweetSerializer

    def get_queryset(self):
        CONSUMER_KEY = 'L34y0Ez744ifincFlkzqLus57'
        CONSUMER_SECRET = 'c99M7ymvB5B74p16aAu70YZPbJaRx0VP48hW2UJoN8KNOs7hr8'
        ACCESS_KEY = '1104063783234879490-kY0DJFnHf29bT11WdvMspTqbGvHqST'
        ACCESS_SECRET = 'DrHQf9AztSRwJPmDRXjURkFiLx8YmVM23A96C2Ac0xUwd'
        query = self.request.query_params.get('query')
        auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        search_results = api.search(q=str(query), count=10)
        results = []
        for i in search_results:
            results.append(Tweet(user=i._json['user']['screen_name'], image=i._json['user']['profile_image_url_https'],
                                 text=i._json['text'], created=i._json['created_at'], id_tw=i._json['id']))

        return results


