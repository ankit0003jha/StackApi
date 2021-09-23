from django.shortcuts import render ,redirect
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.throttling import  AnonRateThrottle
from rest_framework.decorators import api_view, throttle_classes
import requests
import json
import time

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
call_count = None
TIME_PERIOD = 300   # time period in seconds
start_time = time.time()



@api_view(['GET'])
@throttle_classes([AnonRateThrottle,])
def profile(request, count = [0]):
    if request.GET:
        throttle_scope = 'search'
        query = request.GET['query']
        order = request.GET['order']
        pages = request.GET['page']
        pagesize = request.GET['pagesize']
        title = request.GET['title']
        body = request.GET['body']
        view = request.GET['view']
        answer = request.GET['answer']
        url = request.GET['url']
        sort = request.GET['sort']
        accept = request.GET['accept']
        closed = request.GET['closed']
        migrate = request.GET['migrated']
        wiki = request.GET['wiki']
        notice = request.GET['notice']
        fromdate = request.GET['fromdate']
        todate = request.GET['todate']
        mini = request.GET['min']
        maxi = request.GET['max']
        user = request.GET['user']
        tagged = request.GET['tagged']
        nottagged = request.GET['nottagged']

        if cache.get(query):
            CacheData = cache.get(query)
            stackdata = []
            for title in CacheData['items']:
                     stackdata.append(title)
            paginator = Paginator(stackdata, 5)
            pageNumber = request.GET.get('page')
            page = paginator.get_page(pageNumber)
            print('DATA FROM CACHE')
            return render( request, 'index.html', {'data':page, "query": query, "order": order, "page": pages, "pagesize": pagesize, "title": title, "body": body, "view": view, "answer": answer, "url": url, "sort": sort, "accept": accept, "closed": closed, "migrate": migrate, "wiki": wiki, "notice": notice, "min": mini, "maxi": maxi, "user": user, "todate": todate, "fromdate": fromdate, "tagged": tagged, "nottagged": nottagged})
        else:
            response = requests.get('https://api.stackexchange.com/2.2/search/advanced?page=' + pages + '&pagesize=' + pagesize + '&fromdate=' + fromdate + '&todate=' + todate + '&order=' + order + '&min=' + mini + '&max=' + maxi + '&sort=' + sort + '&q=' + query + '&accepted=' + accept + '&answers=' + answer + '&body=' + body + '&closed=' + closed + '&migrated=' + migrate + '&notice=' + notice + '&nottagged=' + nottagged + '&tagged=' + tagged + '&title=' + title + '&user=' + user + '&url=' + url + '&views=' + view + '&wiki=' + wiki + '&site=stackoverflow')
            apiResponse = response.json()
            cache.set(query, apiResponse)
            print('DB DATA')
            stackdata = []
            for title in apiResponse['items']:
                 stackdata.append(title)
            paginator = Paginator( stackdata, 5)
            pageNumber = request.GET.get('page')
            page = paginator.get_page(pageNumber)
            
            return render( request, 'index.html', {'data':page, "order": order, "page": pages, "pagesize": pagesize, "title": title, "body": body, "view": view, "answer": answer, "url": url, "sort": sort, "accept": accept, "closed": closed, "migrate": migrate, "wiki": wiki, "notice": notice, "min": mini, "maxi": maxi, "user": user, "todate": todate, "fromdate": fromdate, "tagged": tagged, "nottagged": nottagged})
    else:
        return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')