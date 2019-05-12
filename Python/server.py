
import tornado.ioloop
import tornado.web
import tornado.escape
import json
myport = 8888
from . import connector
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        print("hello")
        args = tornado.escape.json_decode(self.request.body)
        # print(args)
        content = json.loads(args)
        print(content)
        connector.insertWeatherData(content)

        # print(args)
        # temperature = content["temperature"]
        # wind = content["wind"]
        # country = content["country"]
        # city = content["city"]
        #
        # print("Temperaturka:{}, wiaterek: {}, państwo: {}, miasteczko: {}".format(temperature, wind, country, city))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(myport)
    tornado.ioloop.IOLoop.current().start()