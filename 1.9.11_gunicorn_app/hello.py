import pprint

# 'PATH_INFO': '/hello',
# 'QUERY_STRING': 'a=12&b=1&b=2',

def app(environ, start_response):
    pprint.pprint(environ)
    vars = environ['QUERY_STRING'].split("&")
    data = '\n'.join(vars) + '\n'
    data = data.encode('utf-8')
    # data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
#        ("Content-Length", str(len(data)))
    ])

    return iter([data])
