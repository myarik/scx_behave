# -*- coding: utf-8 -*-
import codecs
import socket
from time import sleep

import requests

requests_session = requests.session()

socket.setdefaulttimeout(60)


def file_get_content(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


def get_content(url, params=None, as_json=True,
                post=False, use_sessions=False, headers=None,
                retries=3, retry_pause=10, timeout=10):
    """
    Function to get info from social network
    Args:
        url: url
        retries: int number of retries.
        retry_pause: int number of seconds to pause between retries
    Returns:
        content or None
    """
    if use_sessions:
        req = requests_session
    else:
        req = requests
    retry = 0
    r = None
    while retry < retries:
        try:
            if post:
                r = req.post(
                    url=url,
                    data=params,
                    timeout=timeout,
                    headers=headers
                )
            else:
                r = req.get(
                    url=url,
                    params=params,
                    timeout=timeout,
                    headers=headers
                )
            if 500 <= r.status_code < 600:
                raise requests.exceptions.HTTPError
            return r
        except (
                requests.exceptions.Timeout,
                requests.exceptions.HTTPError,
                requests.exceptions.ConnectionError
        ):
            retry += 1
            if retry < retries:
                sleep(retry_pause)
    return r


def build_absolute_uri(request, location, protocol=None):
    uri = request.build_absolute_uri(location)
    if protocol:
        uri = protocol + ':' + uri.partition(':')[2]
    return uri


def extract_hash_tags(text):
    """
    Find tags in text
    :param text:
    :return: list with tags
    :Example
        "Well here it is... #HamptonsBound #NYFWM"
        return [HamptonsBound, NYFWM]
    """
    if text:
        return list(
            set(part[1:] for part in text.split() if part.startswith('#')))
    return []
