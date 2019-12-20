#!/usr/bin/python
# -*- coding: utf-8 -*-

from thumbor.loaders import http_loader
from tornado.concurrent import return_future
from thumbor.utils import logger
import base64


def decode_url(url):
    url = http_loader.quote_url(url)
    try:
        url_bytes = url.encode('ascii')
        urlSafeEncodedBytes = base64.urlsafe_b64decode(url_bytes)
        urlSafeEncodedStr = str(urlSafeEncodedBytes)
        return urlSafeEncodedStr.decode('ascii')
    except:
        return url


def _normalize_url(url):
    url = decode_url(url)
    return url if url.startswith('http') else 'https://%s' % url


def validate(context, url):
    return http_loader.validate(context, url, normalize_url_func=_normalize_url)


@return_future
def load(context, url, callback):
    return http_loader.load_sync(context, url, callback, normalize_url_func=_normalize_url)
