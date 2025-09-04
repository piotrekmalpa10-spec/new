import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests




class Home:
    def __init__(self, driver):
        self.driver = driver


    def load(self):
        self.driver.get('https://duckduckgo.com/')

    def search(self):
        s = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchbox_input')))
        s.send_keys('fakeapistore')
        s.send_keys(Keys.RETURN)

    def click_(self):
        c = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')))
        c.click()


@pytest.fixture
def driver():
    drive = webdriver.Chrome()
    yield drive
    drive.maximize_window()
    drive.close()