
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Assumes Chrome WebDriver is installed
    yield driver
    driver.quit()

def test_frontend_title(browser):
    browser.get('http://localhost:3000')
    assert 'Agent Market' in browser.title

def test_frontend_header(browser):
    browser.get('http://localhost:3000')
    header = browser.find_element(By.TAG_NAME, 'h1')
    assert header.text == 'Agent Market'
