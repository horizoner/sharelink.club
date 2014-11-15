from django.shortcuts import render_to_response
from sharelink.linkhome.models import LinkHome as lh

def index(req):
    if req.method == 'POST':
        new_link = lh(url = req.POST['url'], title = req.POST['title'])
        new_link.save()
    links = lh.objects.all()
    print links
    return render_to_response('index.html', {'links': links})
