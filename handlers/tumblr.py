# -*- coding: utf-8 -*-


class Tumblr(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@id="content_postimg_inner"]'):
            return div[0].text_content()
        return None