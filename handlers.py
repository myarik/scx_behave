# -*- coding: utf-8 -*-

class Handlers(object):
    @staticmethod
    def handle(lhtml):
        elements = [
            '//*[@id="home-main"]',
            '//*[@class="post-content-container"]',
            '//*[@class="post-alt blog"]',
            '//*[@id="content"]',
            '//*[@id="content_postimg_inner"]',
            '//*[@id="wi-content"]',
            '//*[@class="post-outer"]',
            '//*[@class="single col-xs-12 col-md-8"]',
            '//*[@id="content-area"]',
            '//*[@class="bella"]',
            '//*[@class="main-wrapper"]',
            '//*[@id="main-wrapper"]',
            '//*[@class="section"]',
            '//*[@class="posts"]',
            '//*[@id="contentinner_lt"]',
            '//*[@id="thePosts"]',
            '//*[@class="content"]',
            '//*[@id="blogroll"]',
            '//*[@id="main"]',
            '//*[@class="entry-content"]',
            '//*[@class="main-content-column-1"]',
        ]
        for element in elements:
            final = ''
            for div in lhtml.xpath(element):
                    final += div[0].text_content()
            if final:
                # import codecs
                # with codecs.open('catch.txt', 'w', 'utf-8') as f:
                #     f.write(element)
                # with codecs.open('out.txt', 'w', 'utf-8') as f:
                #     f.write(final)
                return final

        return None
