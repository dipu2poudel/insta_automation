from selenium import webdriver


def get_chrome_web_driver(options):
    return webdriver.Chrome("chromedriver.exe", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def disable_security(options):
    options.add_argument("--disable-infobars")

    options.add_argument("start-maximized")

    options.add_argument("--disable-extensions")
    preference = {"profile.default_content_setting_values.geolocation": 1}
    options.add_experimental_option("prefs", preference)


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito_and_no_geo(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
