# -*- coding: utf-8 -*-


class Sydnestyle(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@class="single col-xs-12 col-md-8"]'):
            return div[0].text_content()
        return None