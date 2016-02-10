# -*- coding: utf-8 -*-


class Divalicious(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@id="content-area"]'):
            return div[0].text_content()
        return None
