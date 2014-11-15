import json
from django.shortcuts import render_to_response
from django.http import HttpResponse

from sharelink.linkhome.models import LinkHome as lh
from sharelink.linkhome.crawer import Crawer

def index(req):
    links = lh.objects.all()
    return render_to_response('index.html', {'links': links})

def add_link(req):
    if req.method == 'POST':
        url = req.POST.get('url')
        title = req.POST.get('title')
        if check_data(url, title):
            # save into db if the data is validate
            result = save_link(url, title)
            # craw the webpage snapshot
            # get_snapshot(url)
        else:
            result = {'success': False, 'error': 'Invalid data'}
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
    return True if url and title else False

def crawer(req):
    '''
    linux crontab task trigger craw event
    '''
    # pass
    link = lh.objects.get(title = 'baidu')
    crawer = Crawer(link.url)
    crawer.run()
    return HttpResponse('crawwing...')
