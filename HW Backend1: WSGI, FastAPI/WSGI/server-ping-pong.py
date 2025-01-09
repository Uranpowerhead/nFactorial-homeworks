def app(environ, start_response):
    path = environ.get('PATH_INFO')
    method = environ.get('REQUEST_METHOD')

    if method == 'GET' and path == '/ping':
        data = b"pong"
        start_response('200 OK', [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))])
        return iter([data])
    else:
        data = b"Not Found"
        start_response('404 Not Found', [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))])
        return iter([data])