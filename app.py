def application(environ, start_response):
    """Simple WSGI application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    # Return path
    path = environ['PATH_INFO']

    return [f'Hello, World! You requested {path}'.encode('utf-8')]
