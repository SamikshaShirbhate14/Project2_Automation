from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://iemodemoindia.meditab.com")
    return driver