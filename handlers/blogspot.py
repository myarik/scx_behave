# -*- coding: utf-8 -*-


class Blogspot(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@class="post-outer"]'):
            return div[0].text_content()
        return None
