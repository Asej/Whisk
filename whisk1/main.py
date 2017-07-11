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
        base_url = "http://www.recipepuppy.com/api/?"
        url_params = {'q': self.request.get("answer")}
        giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        template = jinja_environment.get_template('pages/results.html')

        self.response.out.write(template.render())
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results.html', ResultHandler),
])
