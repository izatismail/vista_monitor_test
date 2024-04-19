import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am already on the "Dürr Dental ID" login page')
def step_impl(context):
    # Assert to confirm the current page if needed for additional safety
    assert context.browser.title == "Dürr Dental ID", "Not on the 'Dürr Dental ID' login page"


@when('I enter "{email}" as the email and "{password}" as the password')
def step_impl(context, email, password):
    login_username = os.getenv(email)  # Environment variable for the email
    login_pwd = os.getenv(password)  # Environment variable for the password

    email_input = context.browser.find_element(By.ID, "username")
    email_input.clear()
    email_input.send_keys(login_username)

    password_input = context.browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(login_pwd)


@when('I submit the login form')
def step_impl(context):
    submit_button = context.browser.find_element(By.NAME, "login")
    submit_button.click()


@then('I should be redirected to the VSM dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://vsmonitor.com/dashboard")
    )

    dashboard_element = context.browser.find_element(By.CLASS_NAME, "_tid_dashboard")
    assert dashboard_element, "Dashboard element is missing."

