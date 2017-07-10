import json
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pages/first.html')
        self.response.write('pages/first.html')
class ResultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results', ResultHandler),
], debug=True)
