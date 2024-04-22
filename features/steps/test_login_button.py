from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.utilities import config as util_cfg
from features.utilities import site_navigator as util_nav
from features.utilities import common_actions as util_ca


@given('I am on the VSM homepage')
def step_impl(context):
    util_nav.go_to_page(context, util_cfg.URLConfig.HOMEPAGE)


@when('I click on the Login button')
def step_impl(context):
    util_ca.click_login_button(context)


@then('I should be on the "Dürr Dental ID" login page')
def step_impl(context):
    # Now perform the assertion to check the page title
    assert context.browser.title == util_cfg.PageTitle.LOGIN, \
                        f"Expected page title to be {util_cfg.PageTitle.LOGIN}, but it was '{context.browser.title}'"

    # Wait for all elements matching the CSS selector to be visible on the page
    headers = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h1[aria-label='heading']"))
    )

    found = any("Log-in" in header.text for header in headers)
    assert found, "No header contains 'Log-in'"
