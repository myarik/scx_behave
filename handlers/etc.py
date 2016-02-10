# -*- coding: utf-8 -*-


class Etc(object):
    @staticmethod
    def handle(lhtml):
        for div in lhtml.xpath('//*[@class="section"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@id="contentinner_lt"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@id="thePosts"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@class="content"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@id="blogroll"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@id="main"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@class="entry-content"]'):
            return div[0].text_content()

        for div in lhtml.xpath('//*[@class="main-content-column-1"]'):
            return div[0].text_content()





        return None