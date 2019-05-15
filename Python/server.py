
import tornado.ioloop
import tornado.web
import tornado.escape
import json
myport = 8888
from connector import insertWeatherData
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        print("hello")
        args = tornado.escape.json_decode(self.request.body)
        content = json.loads(args)
        print(content)
        connector.insertWeatherData(content)
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(myport)
    tornado.ioloop.IOLoop.current().start()