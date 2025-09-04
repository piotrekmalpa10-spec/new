from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import asyncio
import requests


class Home:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://duckduckgo.com/')

    def search(self, text):
        w = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'searchbox_input')))

        w.send_keys(text)
        w.send_keys(Keys.RETURN)

    def click_to_link(self):
        w = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')))

        w.click()

    def click_to_products(self):
        d = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="btn btn-primary"]')))
        d.click()

    def cilck_products(self):
        d = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class='sc-bpUBKd itmOnH']")))
        d.click()
        

@pytest.fixture
def driver():
    drive  = webdriver.Chrome()
    
    yield drive
    
    drive.close()

def test_home(driver):
    h = Home(driver)

    h.search('fakestore api')
    h.click_to_link()
    h.click_to_products()
    h.cilck_products()

def test_req():
    res = requests.get('https://fakestoreapi.com/products/1')

    assert res.status_code == 200

    assert res.json() == {"id":1,"title":"Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops","price":109.95,"description":"Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday","category":"men's clothing","image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png","rating":{"rate":3.9,"count":120}}