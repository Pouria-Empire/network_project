import socketserver as SocketServer
import http.server as SimpleHTTPServer
from urllib.request import urlopen
PORT = 8081

class MyProxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urlopen(url), self.wfile)


httpd = SocketServer.ForkingTCPServer(('', PORT), MyProxy)
print("Now serving at "+str(PORT))
httpd.serve_forever()