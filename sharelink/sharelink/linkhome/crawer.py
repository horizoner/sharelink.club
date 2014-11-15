import threading

class Crawer(object):
    url = None

    def __init__(self, url):
        self.url = url

    def run(self):
        print 'Crawer running...'
        print 'Fetching %s' % self.url

    def stop(self):
        pass

