# -*- coding: utf-8 -*-


class Beauty411(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@id="wi-content"]'):
            return div[0].text_content()
        return None