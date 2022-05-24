import ssl
from six.moves.urllib_request import HTTPSHandler
from six.moves.http_client import HTTPSConnection

class HTTPSClientAuthHandler(HTTPSHandler):
    def __init__(self):
        HTTPSHandler.__init__(self)
        ssl._create_default_https_context = ssl._create_unverified_context

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        context = ssl._create_unverified_context(ssl.PROTOCOL_TLSv1_2)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return HTTPSConnection(host, timeout=timeout, context=context)
