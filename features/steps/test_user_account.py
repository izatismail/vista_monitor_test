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
    # debugging, to see if element is clickable
    profile_icon = context.browser.find_element(By.XPATH, "//div[@aria-label='nav-user-button']")
    WebDriverWait(context.browser, 20).until(
        lambda x: profile_icon.is_displayed() and profile_icon.size['height'] > 0 and profile_icon.size['width'] > 0
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", profile_icon)


    # Then use ActionChains to perform the hover
    hover = ActionChains(context.browser).move_to_element(profile_icon)
    hover.perform()
    hover.click(profile_icon).perform()


    # both attempt using wait then click and force js failed
    #WebDriverWait(context.browser, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='nav-user-button']"))
    #).click()
    #context.browser.execute_script("arguments[0].click();", element)


@when('I click on the "My user account"')
def step_impl(context):
    # Wait for the dropdown to be visible and interactable
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='select-item-user-profile']"))
    )

    # Click on the dropdown item for "My user account"
    user_account_option = context.browser.find_element(By.ID, "user-profile")
    user_account_option.click()


@then('I should see "My user account" menu')
def step_impl(context):
    # This could be validated by checking the URL or a specific element on the page
    assert context.browser.current_url == "https://vsmonitor.com/user/profile", \
        f"Expected URL to be 'https://vsmonitor.com/user/profile' but was {context.browser.current_url}"

    assert context.browser.title == "My user account" in context.browser.title


@then('I should see "My user account" page')
def step_impl(context):
    # This could be validated by checking the URL or a specific element on the page
    assert context.browser.current_url == "https://vsmonitor.com/user/profile", \
        f"Expected URL to be 'https://vsmonitor.com/user/profile' but was {context.browser.current_url}"

    assert context.browser.title == "My user account" in context.browser.title, "Not on My user account page."


@then('I should see correct name and email address')
def step_impl(context):
    # Assume data is retrieved from database. The following is hardcoded for PoC
    correct_fname = "Shahrizat"
    correct_lname = "Ismai"
    correct_email = "izatismail@gmail.com"

    first_name_element = context.browser.find_element(By.ID, "firstName")
    last_name_element = context.browser.find_element(By.ID, "lastName")
    email_element = context.browser.find_element(By.ID, "email")

    assert first_name_element.text == correct_fname, f"Expected first name {correct_fname}, but found {first_name_element}"
    assert last_name_element.text == correct_lname, f"Expected last name {correct_lname}, but found {last_name_element}"
    assert email_element.text == correct_email, f"Expected email {correct_email}, but found {email_element.text}"
