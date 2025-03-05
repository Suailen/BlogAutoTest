import time

from selenium.webdriver.common.by import By

from common.Utils import BlogDriver


class BlogList:
    def __init__(self):
        self.driver=BlogDriver.driver
        self.url="http://8.137.19.140:9090/blog_list.html"
        self.driver.get(self.url)

    #测试首页（登录状态下）
    def ListTestByLogin(self):
        #检查左侧用户信息
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > img")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > a")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(4) > span:nth-child(1)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(5) > span:nth-child(1)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(4) > span:nth-child(2)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > div:nth-child(5) > span:nth-child(2)")

        #检查右侧博客列表
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div:nth-child(1) > div.title")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div:nth-child(1) > div.date")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div:nth-child(1) > div.desc")
        #点击“查看全文”按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div:nth-child(1) > a").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.right > div > div.title")
        self.driver.back()

        #检查上方菜单栏
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > img")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > span")
        #点击“写博客”按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR,"#title")
        time.sleep(1)
        BlogDriver.ScreenShot()
        #点击“主页”按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        time.sleep(1)
        BlogDriver.ScreenShot()

    #测试首页（未登录状态）
    def ListTestByNotLogin(self):
        #点击“注销”按钮
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(6)").click()
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container-login > div > h3")
        BlogDriver.ScreenShot()
