import json
import jinja2
import os
import webapp2
import random
import urllib2
import urllib

class MainHandler(webapp2.RequestHandler):
    def get(self):
    self.response.out.write('Hello world!')
class ResultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results', ResultHandler),
], debug=True)
