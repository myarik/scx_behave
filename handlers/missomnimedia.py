# -*- coding: utf-8 -*-


class Missomnimedia(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@class="post-alt blog"]'):
            return div[0].text_content()
        return None