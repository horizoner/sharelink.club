import json
import urllib2
from django.shortcuts import render_to_response
from django.http import HttpResponse

from sharelink.linkhome.models import LinkHome as lh
from sharelink.linkhome.crawler import Crawler

def index(req):
    links = lh.objects.all()
    return render_to_response('index.html', {'links': links})

def add_link(req):
    if req.method == 'POST':
        url = req.POST.get('url')
        title = req.POST.get('title')
        check_result = check_data(url, title)
        if check_result['success']:
            # save into db if the data is validate
            result = save_link(url, title)
            # craw the webpage snapshot
            # get_snapshot(url)
        else:
            result = {'success': False, 'error': check_result['error']}
        return HttpResponse(json.dumps(result), content_type = "application/json")
    else:
        # redirect to index
        # pass
        return HttpResponse('403 Forbidden')

def save_link(url, title):
    try:
        new_link = lh(url = url, title = title)
        new_link.save()
        return {'success': True}
    except Exception, e:
        return {'success': False, 'error': 'Database error: %s' % e }

def check_data(url, title):
    '''
    validate the post data
    '''
    result = {'error': ''}
    if title:
        pass
    try:
        urllib2.urlopen(url, timeout = 3)
        result['success'] = True
    except Exception, e:
        result['success'] = False
        result['error'] += 'invalid URL.'
    return result

def crawler(req):
    '''
    linux crontab task trigger crawl event
    '''
    # pass
    link = lh.objects.get(title = 'baidu')
    crawler = Crawler(link.url)
    crawler.run()
    return HttpResponse('crawling...')

def get_snapshot(req):
    # url_id = int(req.POST.get('id'))
    url_id = 1
    try: 
        row = lh.objects.get(url = 'http://www.baidu.com') 
    except Exception, e:
        print 'Error: ', e
        row = e
    # row = lh.objects.all()
    print type(row)
    return HttpResponse(row)

















