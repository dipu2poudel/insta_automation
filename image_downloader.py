from selenium import webdriver
from web_driver_conf import get_web_driver_options
from web_driver_conf import get_chrome_web_driver
from web_driver_conf import set_ignore_certificate_error
from web_driver_conf import set_browser_as_incognito_and_no_geo
from web_driver_conf import disable_security
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests


def download_all_images(hashtag):
    options = get_web_driver_options()
    set_ignore_certificate_error(options)
    set_browser_as_incognito_and_no_geo(options)
    disable_security(options)
    driver = get_chrome_web_driver(options)
    driver.get('https://www.instagram.com/explore/tags/woodwork/')
    images_link = driver.find_elements_by_class_name('FFVAD')
    reduced_image_link = []
    for i in range(10):
        reduced_image_link.append(images_link[i])
    href_links = []
    i = 0
    for link in reduced_image_link:
        i += 1
        href_link = link.get_property('src')
        print(href_link)
        # href_links.append(link.get_property('src'))
        response = requests.get(href_link)
        file = open(f"images/{i}.jpeg", "wb")
        file.write(response.content)
        file.close()
        if i > 5:
            break


download_all_images('#woodwork')

print("---completed---")
