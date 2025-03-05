import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.Utils import BlogDriver

class BlogLogin:
    def __init__(self):
        self.url="http://8.137.19.140:9090/blog_login.html"
        self.driver=BlogDriver.driver
        self.driver.get(self.url)
    def LoginSuc(self):
        username=self.driver.find_element(By.CSS_SELECTOR,"#username")
        password=self.driver.find_element(By.CSS_SELECTOR,"#password")
        username.clear()
        password.clear()
        username.send_keys("zhangsan")
        password.send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        BlogDriver.ScreenShot()
        #如果登录成功，则能找到昵称
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.back()

    def LoginFail(self):
        #输入正确的用户名和错误的密码
        username = self.driver.find_element(By.CSS_SELECTOR, "#username")
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        username.clear()
        password.clear()
        username.send_keys("zhangsan")
        password.send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        assert alert.text=="密码错误"
        alert.accept()
        BlogDriver.ScreenShot()

        #输入错误的用户名和正确的密码
        username.clear()
        password.clear()
        username.send_keys("wangwu")
        password.send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        assert alert.text=="用户不存在"
        alert.accept()
        BlogDriver.ScreenShot()

        # 输入错误的用户名和错误的密码
        username.clear()
        password.clear()
        username.send_keys("wangwu")
        password.send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == "用户不存在"
        alert.accept()
        BlogDriver.ScreenShot()


