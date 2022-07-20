import pytest
from selenium import webdriver
import time

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    #time.sleep(5)
    #browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()