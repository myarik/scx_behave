import codecs
import re

import requests_mock
from behave import *

from parser.blog_parser import BlogParser


def file_get_content(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


@when("I visit url {url} in file {file_name}")
def step_impl(context, url, file_name):
    with requests_mock.Mocker() as m:
        m.get(url, text=file_get_content('files/{file_name}'.format(file_name=file_name)))
        blog_parser = BlogParser(url)
        context.content = blog_parser.get_content()


@then("I should see {text}")
def step_impl(context, text):
    assert bool(re.search(text, context.content))


@then("I shouldn't see {text}")
def step_impl(context, text):
    assert not bool(re.search(text, context.content))
