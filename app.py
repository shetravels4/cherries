from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Murat's Azure World!"

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

'''import logging

import web
from web.httpserver import StaticMiddleware

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
main_logger = logging.getLogger('main_log')

urls = (
    '/z-path/monitor', 'monitoring',
    '/test-server/test', 'server_test',
    '/favicon.ico', 'dummy',
    '/*', 'index'
)

class index:
    def GET(self):
        main_logger.info("CALLED: class index:")
        return "Index function GET request, handling /*"

class dummy:
    def GET(self):
        main_logger.info("CALLED: class dummy")
        return "Dummy function GET request, handling /favicon.ico"

class server_test:
    def GET(self):
        main_logger.info("CALLED: class server_test")
        x = "This is a test"
        return x

class monitoring:
    def GET(self):
        main_logger.info("CALLED: class monitoring")
        return "The server is running"

class MyStaticMiddleware(StaticMiddleware):
    def __init__(self, app, prefix='/z-path/'):
        StaticMiddleware.__init__(self, app, prefix)

app = web.application(urls, globals())
if __name__ == '__main__':
    app.run(port=8889)
wsgiapp = web.application(urls, globals()).wsgifunc()
'''