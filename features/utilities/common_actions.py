import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -------- HELPER ----------------------------------------------------------------------------------
def __click_element(context, locator):
    element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(locator)
    )

    element.click()


# ----------- CLICKS -----------------------------------------------------------------------------
def click_login_button(context):
    xpath = "//button[contains(@aria-label, 'btn-sso') and contains(., 'Login')]"
    login_button_locator = (By.XPATH, xpath)

    __click_element(context, login_button_locator)


def click_submit_login(context):
    submit_button = context.browser.find_element(By.NAME, "login")
    submit_button.click()


# ----------- FILLS -----------------------------------------------------------------------------

def fill_in_login(context, email, password):
    login_username = os.getenv(email)  # Environment variable for the email
    login_pwd = os.getenv(password)  # Environment variable for the password

    email_input = context.browser.find_element(By.ID, "username")
    email_input.clear()
    email_input.send_keys(login_username)

    password_input = context.browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(login_pwd)


