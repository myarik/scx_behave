# -*- coding: utf-8 -*-

import re

import lxml.html

from handlers import Handlers
from socialapp.utils import get_content


class BlogParser(object):
    def __init__(self, link):
        self.link = link
        self.handlers = []
        self._register(Handlers)

    def _register(self, handler):
        self.handlers.append(handler)

    def _handle_all(self, lhtml):
        for handler in self.handlers:
            content = handler.handle(lhtml)
            if content:
                return content
        final = lhtml.text_content()
        result = re.search('(.+?)comments', final, re.IGNORECASE)
        if result:
            final = result.group(1)
        return final

    def get_content(self):
        """
        Returns:
            Plain content of the page without (str) if parsing successful, False (bool) otherwise
        """
        response = get_content(self.link)

        if response and response.status_code == 200:
            lhtml = lxml.html.fromstring(response.content)

            # for bad in lhtml.xpath('//script'):
            #     bad.getparent().remove(bad)
            for bad in lhtml.xpath('//style'):
                bad.getparent().remove(bad)
            for bad in lhtml.xpath('//head'):
                bad.getparent().remove(bad)

            return self._handle_all(lhtml)
        return ''
