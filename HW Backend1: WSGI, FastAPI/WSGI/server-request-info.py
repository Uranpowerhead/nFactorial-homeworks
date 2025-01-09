def app(environ, start_response):
    path = environ.get('PATH_INFO')
    method = environ.get('REQUEST_METHOD')

    if method == 'GET' and path == '/info':
        method = environ.get('REQUEST_METHOD')
        url = environ.get('PATH_INFO')
        protocol = environ.get('SERVER_PROTOCOL')

        data = f"HTTP Method: {method}\nURL: {url}\nProtocol: {protocol}".encode('utf-8')
        start_response('200 OK', [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))])
        return iter([data])

    else:
        data = b"Not Found"
        start_response('404 Not Found', [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))])
        return iter([data])