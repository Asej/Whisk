
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
class ResultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/results', ResultHandler),
], debug=True)
