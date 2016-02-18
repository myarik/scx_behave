import codecs

import requests_mock
from behave import *

from blog_parser import BlogParser


def file_get_content(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


@requests_mock.Mocker()
@when("I visit url {url} in file {file}")
def step_impl(context, url, file):
    with requests_mock.Mocker() as m:
        m.get(url, text=file_get_content('files/{file}'.format(file=file)))
        blog_parser = BlogParser(url)
        context.content = blog_parser.get_content()


@then("I should see {text}")
def step_impl(context, text):
    assert text in context.content


@then("I should not see {text}")
def step_impl(context, text):
    assert not text in context.content
