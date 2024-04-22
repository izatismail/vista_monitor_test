from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from features.utilities.config import URLConfig


def go_to_page(context, page_url):
    context.browser.get(page_url)
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Wait for the page to load
    )
