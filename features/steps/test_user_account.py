import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.utilities import config as util_cfg
from features.utilities import site_navigator as util_nav
from features.utilities import common_actions as util_ca


@given('I am on the VSM dashboard page')
def step_impl(context):
    util_nav.go_to_page(context, util_cfg.URLConfig.DASHBOARD)

    # need to login if failed to load dashboard
    if context.browser.title != util_cfg.PageTitle.DASHBOARD:
        util_nav.go_to_page(context, util_cfg.URLConfig.HOMEPAGE)
        util_ca.click_login_button(context)

        WebDriverWait(context.browser, 15).until(
            EC.title_is(util_cfg.PageTitle.LOGIN)
        )
        util_ca.fill_in_login(context, "VSM_EMAIL", "VSM_PWD")
        util_ca.click_submit_login(context)

        WebDriverWait(context.browser, 10).until(
            EC.url_to_be(util_cfg.URLConfig.DASHBOARD)
        )


@when('I click on the profile button')
def step_impl(context):
    profile_icon = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-desktop ._tid_nav-user-button .flex"))
    )

    profile_icon.click()


@when('I click on the "My user account"')
def step_impl(context):
    user_account_menu = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-profile > .truncate"))
    )

    user_account_menu.click()


@then('I should see "My user account" page')
def step_impl(context):
    WebDriverWait(context.browser, 15).until(
        EC.title_is(util_cfg.PageTitle.USER_ACCOUNT)
    )

    assert context.browser.current_url == util_cfg.URLConfig.USER_ACCOUNT, \
                        f"Expected URL to be {util_cfg.URLConfig.USER_ACCOUNT} but was {context.browser.current_url}"


@then('I should see correct name and email address')
def step_impl(context):
    # Assume data is retrieved from database. The following is hardcoded for PoC
    correct_fname = "Shahrizat"
    correct_lname = "Ismai"
    correct_email = "izatismail@gmail.com"

    # Locate the input element and get its value
    first_name_input = context.browser.find_element(By.ID, "firstName")
    first_name_value = first_name_input.get_attribute('value')

    last_name_input = context.browser.find_element(By.ID, "lastName")
    last_name_value = last_name_input.get_attribute('value')

    email_input = context.browser.find_element(By.ID, "email")
    email_value = email_input.get_attribute('value')

    assert first_name_value == correct_fname, f"Expected first name {correct_fname}, but found {first_name_element}"
    assert last_name_value == correct_lname, f"Expected last name {correct_lname}, but found {last_name_element}"
    assert email_value == correct_email, f"Expected email {correct_email}, but found {email_element.text}"
