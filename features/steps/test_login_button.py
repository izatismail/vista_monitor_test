from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the VSM homepage')
def step_impl(context):
    context.browser.get("https://vsmonitor.com")


@when('I click on the Login button')
def step_impl(context):
    xpath = "//button[contains(@aria-label, 'btn-sso') and contains(., 'Login')]"
    login_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    login_button.click()


@then('I should be on the "Dürr Dental ID" login page')
def step_impl(context):
    # Now perform the assertion to check the page title
    assert context.browser.title == "Dürr Dental ID", f"Expected page title to be 'Dürr Dental ID', but it was '{context.browser.title}'"

    # Wait for all elements matching the CSS selector to be visible on the page
    headers = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h1[aria-label='heading']"))
    )

    found = any("Log-in" in header.text for header in headers)
    assert found, "No header contains 'Log-in'"
