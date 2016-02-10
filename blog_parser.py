# -*- coding: utf-8 -*-

import lxml.html

from handlers import (Wordpress, Blogspot, Divalicious, Beauty411, Missomnimedia, Sydnestyle, Tumblr, Etc)
from utils import get_content


class BlogParser(object):
    def __init__(self, link):
        self.link = link
        self.handlers = []

        self._register(Blogspot)
        self._register(Wordpress)
        self._register(Divalicious)
        self._register(Beauty411)
        self._register(Missomnimedia)
        self._register(Tumblr)
        self._register(Sydnestyle)
        self._register(Etc)

    def _register(self, handler):
        self.handlers.append(handler)

    def _handle_all(self, lhtml):
        for handler in self.handlers:
            content = handler.handle(lhtml)
            if content:
                return content + ' parsed by ' + str(handler.__class__)
        return lhtml.text_content() + 'NOTPARSED', lxml.html.tostring(lhtml)
        # return lxml.html.tostring(lhtml)

    def get_content(self):
        """
        Returns:
            Plain content of the page without (str) if parsing successful, False (bool) otherwise
        """
        response = get_content(self.link)

        print 2 + 2

        if response and response.status_code == 200:
            lhtml = lxml.html.fromstring(response.content)

            for bad in lhtml.xpath('//script'):
                bad.getparent().remove(bad)
            for bad in lhtml.xpath('//style'):
                bad.getparent().remove(bad)
            for bad in lhtml.xpath('//head'):
                bad.getparent().remove(bad)

            return self._handle_all(lhtml)
        return None
