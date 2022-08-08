import http.server 
import socketserver
class RequestsHandler(http.server.SimpleHTTPRequestHandler):
  """
  Handles http requests
  """
  def do_GET(self):
    if self.path == '/':
      self.path = 'combat.html'
    return http.server.SimpleHTTPRequestHandler.do_GET(self)# Create object of above class
handler_object = RequestsHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)# Start the server
print("Server started at localhost:" + str(PORT))
my_server.serve_forever()