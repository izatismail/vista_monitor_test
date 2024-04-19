from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def before_feature(context, feature):
    context.browser = webdriver.Chrome()


def after_feature(context, feature):
    context.browser.quit()


def before_scenario(context, scenario):
    if "login_page" in scenario.tags:
        if context.browser.title != "Dürr Dental ID":
            context.browser.get("https://vsmonitor.com")
            xpath = "//button[contains(@aria-label, 'btn-sso') and contains(., 'Login')]"
            login_button = WebDriverWait(context.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            login_button.click()
