from behave import *


@when("I visit url {url}")
def step_impl(context, url):
    context.ua.visit(url)


@then("I should see {text}")
def step_impl(context, text):
    assert context.ua.is_text_present(text)


@then("I shouldn't see {text}")
def step_impl(context, text):
    assert not context.ua.is_text_present(text)


@when("I send reset form")
def step_impl(context):
    context.ua.find_by_css('#login-form > fieldset > input').first.click()

@when("I fill email by {email}")
def step_impl(context, email):
    context.ua.find_by_css('#id_email').first.fill(email)