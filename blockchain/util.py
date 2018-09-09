#from .exceptions import *
import sys
import config


py_version = sys.version_info[0]
if py_version >= 3:
    # Python 3.0 and later
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.parse import urlencode
else:
    # Python 2.x
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib import urlencode

import time


def call_api(resource, data=None, base_url=None):
    base_url = config.BASE_URL if base_url is None else base_url
    try:
        payload = None if data is None else urlencode(data)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}

        #req = urllib2.Request(url, data, headers)
        time.sleep(1)
        if py_version >= 3 and payload is not None:
            payload = payload.encode('UTF-8')

        #print (base_url + resource)
        req = Request(base_url + resource)
        #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        #req.add_header('Accept-Encoding','gzip, deflate, br')
        req.add_header('Accept-Language','es-ES,es;q=0.9')
        req.add_header('Cache-Control','max-age=0')
        req.add_header('Connection','keep-alive')
        #req.add_header('Cookie','.AspNetCore.Culture=c%3Den%7Cuic%3Den; __noteCook')
        #req.add_header('Host','smart.ccore.online')
        req.add_header('Upgrade-Insecure-Requests','1')
        req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36')
        #response = urlopen(base_url + resource, payload, timeout=TIMEOUT).read()
        response = urlopen(req,timeout=config.TIMEOUT_URL).read()
        responseutf = response.decode('utf-8')
        return handle_response(responseutf)
    except HTTPError as e:
        raise APIException(handle_response(e.read()), e.code)
    except:
        print ("Fallo , posiblemente por timeout, esperando unos segundos para retomar.")
        time.sleep(10)
        call_api(resource)


def handle_response(response):
    # urllib returns different types in Python 2 and 3 (str vs bytes)
    if isinstance(response, str):
        return response
    else:
        return response.decode('utf-8')
