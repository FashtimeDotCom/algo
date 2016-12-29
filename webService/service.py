# coding:utf-8

import os

import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options

from handle.ia import IaHandle

define("debug", default=False, help="debug mode")
define("port", default=8888, help="run on the given port", type=int)
define("config", default='./conf/test.cfg', help="tornado config file")


class ApplicationIA(tornado.web.Application):
    def __init__(self):
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            }
        handlers = [
            (r'/super/ia', IaHandle),
            ]

        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = ApplicationIA()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

