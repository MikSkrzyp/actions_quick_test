import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    with webdriver.Chrome(options=options) as driver:
        yield driver

def test_google_url(driver):
    driver.get("https://www.google.com")
    assert "google.com" in driver.current_url
