# -*- coding: utf-8 -*-


class Wordpress(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@id="content"]'):
            return div[0].text_content()
        return None
