import json
import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pages/first.html')
        self.response.out.write(template.render())
class ResultHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pages/results.html')

        self.response.out.write(template.render())
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results.html', ResultHandler),
])
