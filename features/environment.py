from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.utilities import config as util_cfg
from features.utilities import site_navigator as util_nav
from features.utilities import common_actions as util_ca


def before_feature(context, feature):
    context.browser = webdriver.Chrome()


def after_feature(context, feature):
    context.browser.quit()


def before_scenario(context, scenario):
    if "login_page" in scenario.tags:
        if context.browser.title != util_cfg.PageTitle.LOGIN:
            util_nav.go_to_page(context, util_cfg.URLConfig.HOMEPAGE)
            util_ca.click_login_button(context)

