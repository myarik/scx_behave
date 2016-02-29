import codecs
import logging

import requests_mock
from behave import *

from blog_parser import BlogParser
from socialapp.utils import file_get_content

bdd = logging.getLogger('bdd')


@requests_mock.Mocker()
@when("I visit url {url} in file {file}")
def step_impl(context, url, file):
    with requests_mock.Mocker() as m:
        m.get(url, text=file_get_content('files/{file}'.format(file=file)))
        blog_parser = BlogParser(url)
        context.content = blog_parser.get_content()


@then("I should see {text}")
def step_impl(context, text):
    if not text in context.content:
        with codecs.open('out.txt', 'w', 'utf-8') as f:
            f.write(context.content)

    assert text in context.content


@then("I should not see {text}")
def step_impl(context, text):
    if text in context.content:
        with codecs.open('out.txt', 'w', 'utf-8') as f:
            f.write(context.content)
    assert not text in context.content
