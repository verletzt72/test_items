import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import *
import time

def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), "Element is not present"