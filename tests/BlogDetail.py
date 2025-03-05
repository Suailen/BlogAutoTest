import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.Utils import BlogDriver


class BlogDetail:
    def __init__(self):
        self.driver=BlogDriver.driver
        self.url="http://8.137.19.140:9090/blog_detail.html?blogId=22196"
        self.driver.get(self.url)

    #测试博客详情页（登录状态）
    def DetailTestByLogin(self):
        #测试左侧用户信息
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > img")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > a")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(4) > span:nth-child(1)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(5) > span:nth-child(1)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(4) > span:nth-child(2)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(5) > span:nth-child(2)")

        #测试右侧博客详情
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.title")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.date")
        self.driver.find_element(By.CSS_SELECTOR,"#detail > p")
        #测试编辑按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.operating > button:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR,"#submit")
        time.sleep(1)
        BlogDriver.ScreenShot()
        self.driver.back()
        #测试删除按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.operating > button:nth-child(2)").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        assert alert.text=="确定删除?"
        alert.dismiss()
        BlogDriver.ScreenShot()

        #测试上方菜单栏
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > img")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > span")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(4)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(5)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(6)")

    # 测试博客详情页（未登录状态）
    def DetailTestByNotLogin(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container-login > div > h3")
        BlogDriver.ScreenShot()