from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credence:
    def test_titlepage_001(self, setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\Screen_Shoots\\test_title page_pass.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screen_Shoots\\test_title page_Fail.png")
            self.driver.close()
            assert False

    def test_logincred_002(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("We are loged In")
            self.driver.save_screenshot(".\\Screen_Shoots\\test_login_pass.png")
            self.driver.close()
            assert True
        except:
            print("Login Failed")
            self.driver.save_screenshot(".\\Screen_Shoots\\test_login_fail.png")
            self.driver.close()
            assert False
