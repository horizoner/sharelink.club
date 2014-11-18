#!/usr/bin/env python

import os
import commands
import threading
from psycopg2 import connect
from time import time
from random import randint

class Crawler(object):
    '''
    get the webpage snapshot with casperjs
    '''
    
    urls = []

    def __init__(self, urls):
        '''
        url is a list
        '''
        self.urls = urls

    def snap(self, url):
        pic_dir = '/home/keith/github/sharelink.club/snapshot/'
        file_name = '%s%s%d.png' % (pic_dir, str(time()), randint(1, 100))
        try:
            success = commands.getoutput('casperjs ./casper.js %s %s' % (url, file_name))
            # print success
            if success == '1':
                print '%s --- %s is OK!' % (url, file_name)
            else:
                print '%s --- %s failed.' % (url, file_name)
        except Exception, e:
            print 'Snap error... ', e


    def run(self):
        threads = []
        for url in self.urls:
            threads.append(threading.Thread(target = self.snap, kwargs = {'url': url}))

        for thread in threads:
            try:
                print '%s started.' % thread
                thread.start()
            except Exception, e:
                print 'error!!!', e

        for thread in threads:
            print '%s end.' % thread
            thread.join()

        print 'all done!'

class DbHelper(object):
    cursor = None

    def __init__(self):
        db = connect(user = 'keith', password = 'keith', dbname = 'sharelink', host = 'localhost')
        self.cursor = db.cursor()

    def query(self):
        sql = "SELECT id, url from links_links limit 5"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_img(path):
        pass

if __name__ == '__main__':
    urls = None
    # urls = ['http://www.baidu.com', 'http://www.v2ex.com', 'https://ipv6.google.com']
    # crawler = Crawler(urls)
    # crawler.run()
    urls = DbHelper()
    print urls.query()
