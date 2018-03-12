from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, json

class Facebook:
    def __init__(self, base_url, wd):
        self.base_url = base_url
        self.wd = wd
        self.wd.get(base_url)

    def login_acc(self, username, password):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="u_0_3"]').click()
        wd.find_element_by_id("email").clear()
        wd.send_keys(username)
        wd.find_element_by_id("password").clear()
        wd.send_keys(password)
        wd.find_element_by_id("loginbutton").click()


    def close(self):
        return self.wd.quit()