from http.server import HTTPServer, BaseHTTPRequestHandler

tasklist = ['Task 1', 'Task 2', 'Task 3'] 

class requestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
      if self.path.endswith('/tasklist'):
          self.send_response(200)
          self.send_header('content-type', 'text/html')
          self.end_headers()
          self.wfile.write(self.path[1:].encode())

          output = ''
          output += '<html><body>'
          output += '<h1>Tak List</h1>'
          output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
          for task in tasklist: 
              output += task
              output += '</br>'
          output += '</body></html>'
          self.wfile.write(output.encode())

      if self.path.endswith('/new'):
          self.send_response(200)
          self.send_header('content-type', 'text/html')
          self.end_headers()


          


def main():
     PORT = 9000
     server_address = ('localhost', PORT)   
     server = HTTPServer(server_address, requestHandler) 
     print('Server running on port %s' % PORT)
     server.serve_forever()

if __name__ == '__main__':
   main()

