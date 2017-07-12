import json
import jinja2
import os
import webapp2 # webapp2 is a module that you import
import random
import urllib2
import urllib

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pages/first.html')
        self.response.out.write(template.render())
class ResultHandler(webapp2.RequestHandler):
    def post(self):
        base_url = "http://www.recipepuppy.com/api/?"
        url_params = {'i': self.request.get("answer"), 'q':'','p':3}
        response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        parsed_dictionary= json.loads(response)
        gif_url = parsed_dictionary['results']
        y=0
        for y in xrange(5):
            name = parsed_dictionary['results'][y]['title']
            self.response.write(name +" "+"<br>")
            ingredients = parsed_dictionary['results'][y]['ingredients']
            self.response.write(ingredients+" "+ "<br>")
            link = parsed_dictionary['results'][y]['href']
            self.response.write(link+" "+"<br>")
            picture = parsed_dictionary['results'][y]['thumbnail']
            self.response.write(picture+" "+"<br>")

            #template = jinja_environment.get_template('pages/results.html')
            #my_title=gif_url["title"]
                ####    my_pict=my_dict[results][i]["thumbnail"]


app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results.html', ResultHandler),
])
