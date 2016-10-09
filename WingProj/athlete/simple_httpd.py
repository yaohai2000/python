from http.server import HTTPServer,CGIHTTPRequestHandler

httpd=HTTPServer(('',8080),CGIHTTPRequestHandler)

print("Starting simple httpd on port: " + str(httpd.server_port))

httpd.serve_forever()