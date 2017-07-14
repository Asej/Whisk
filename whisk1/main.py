import json
import jinja2
import os
import webapp2 # webapp2 is a module that you import
import random
import urllib2
import urllib
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pages/first.html')
        self.response.out.write(template.render())
class ResultHandler(webapp2.RequestHandler):

    def get(self):
        base_url = "http://www.recipepuppy.com/api/?"
        url_params = {'i': self.request.get("ingredients"), 'q':'','p':3}
        response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        parsed_dictionary= json.loads(response)
        gif_url = parsed_dictionary['results']
        food={'name':[],"ingredients":[],'picture':[],'link':[] }

        for y in xrange(10):
             name = parsed_dictionary['results'][y]['title']
             food['name'].append(name)
        #     self.response.write(name +" "+"<br>")
             ingredients = parsed_dictionary['results'][y]['ingredients']
             food['ingredients'].append(ingredients)
        #     self.response.write(ingredients+" "+ "<br>")
             link = parsed_dictionary['results'][y]['href']
             food['link'].append(link)
        #     self.response.write(link+" "+"<br>")
             picture = parsed_dictionary['results'][y]['thumbnail']
             food['picture'].append(picture)
        #    self.response.write(picture+" "+"<br>")


        template = jinja_environment.get_template('pages/results.html')#change html file for template
        self.response.out.write(template.render(food))
        template = jinja_environment.get_template('pages/button.html')#change html file for template
        self.response.out.write(template.render())
            #template = jinja_environment.get_template('pages/results.html')
            #my_title=gif_url["title"]
                ####    my_pict=my_dict[results][i]["thumbnail"]

#class S(ndb.Model):
    #name = ndb.StringProperty()
    #university = ndb.StringProperty()
    #birthday = ndb.DateProperty()

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results', ResultHandler),
])
