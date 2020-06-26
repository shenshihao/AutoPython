from wsgiref.simple_server import make_server


def handle_index():
    return ['<h1>Hello, index!</h1>'.encode('utf-8'), ]


def handle_data():
    return ['<h1>Hello, data!</h1>'.encode('utf-8'), ]


URL_DICT = {
    "/index": handle_index,
    "/data": handle_data
}


def RunServer(environ, start_response):
    # print(environ['path_info'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url = environ['PATH_INFO']
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
    if func:
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8'), ]
    # if current_url == '/index':
    #     return handle_index()
    # elif current_url == '/data':
    #     return handle_data()
    # else:
    #     return ['<h1>404</h1>'.encode('utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
