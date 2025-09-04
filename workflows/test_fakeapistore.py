from home import Home
from home import driver
import pytest







def test_home(driver):
    h = Home(driver)
    h.load()
    h.search()
    h.click_()
