import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.utilities import config as util_cfg
from features.utilities import site_navigator as util_nav
from features.utilities import common_actions as util_ca


@given('I am already on the "Dürr Dental ID" login page')
def step_impl(context):
    # Assert to confirm the current page if needed for additional safety
    assert context.browser.title == util_cfg.PageTitle.LOGIN, "Not on the login page"


@when('I enter "{email}" as the email and "{password}" as the password')
def step_impl(context, email, password):
    util_ca.fill_in_login(context, email, password)


@when('I submit the login form')
def step_impl(context):
    util_ca.click_submit_login(context)


@then('I should be redirected to the VSM dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 15).until(
        EC.url_to_be(util_cfg.URLConfig.DASHBOARD),
        message=f"Expected URL to be {util_cfg.URLConfig.DASHBOARD} but was {context.browser.current_url}"
    )

    dashboard_element = context.browser.find_element(By.CLASS_NAME, "_tid_dashboard")
    assert dashboard_element, "Dashboard element is missing."
