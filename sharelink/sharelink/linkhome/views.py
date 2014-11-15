from django.shortcuts import render_to_response
from django.db.psycopg2 import connection

def index(req):
    if req.method == 'POST':
        print req.POST
        cursor = connection.cursor()
        cursor.execute()
        return render_to_response('index.html', locals())
    else:
        return render_to_response('index.html', {})

