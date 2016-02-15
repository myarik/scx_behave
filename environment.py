# -*- coding: utf-8 -*-

from splinter.browser import Browser


def before_all(context):
    context.ua = Browser()


def after_all(context):
    context.ua.quit()
    context.ua = None
