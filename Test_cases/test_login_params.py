from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class Test_login_params:

    def test_credkart_login_params_001(self, setup, getdataforlogin):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(getdataforlogin[0])
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(getdataforlogin[1])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login done")
            self.driver.save_screenshot(".\\Screen_Shoots\\"+getdataforlogin[0]+"_"+getdataforlogin[1]+"log_pass.png")
            self.driver.close()
            assert True
        except:
            print("Login failed")
            self.driver.save_screenshot(".\\Screen_Shoots\\"+getdataforlogin[0]+"_"+getdataforlogin[1]+"log_fail.png")
            self.driver.close()
            assert False

