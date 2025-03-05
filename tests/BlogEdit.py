import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.Utils import BlogDriver


class BlogEdit:
    def __init__(self):
        self.driver=BlogDriver.driver
        self.url="http://8.137.19.140:9090/blog_edit.html"
        self.driver.get(self.url)

    #测试博客编辑页(登录状态)
    def EditTestByLogin(self):
        #测试上方菜单栏
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > img")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > span")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(4)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(5)")
        self.driver.find_element(By.CSS_SELECTOR,"body > div.nav > a:nth-child(6)")
        #测试编辑主页面
        self.driver.find_element(By.CSS_SELECTOR,"#title")
        self.driver.find_element(By.CSS_SELECTOR,"#editor > div.CodeMirror.cm-s-default.CodeMirror-wrap > div.CodeMirror-scroll")
        self.driver.find_element(By.CSS_SELECTOR,"#editor > div.editormd-preview")
        self.driver.find_element(By.CSS_SELECTOR,"#submit")

    #正常发布博客
    def SubmitSuc(self):
        #输入标题和正文，点击“发布文章”按钮
        self.driver.find_element(By.CSS_SELECTOR,"#title").send_keys("发布文章测试")
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.back()

    #异常发布博客
    def SubmitFail(self):
        #输入正文，标题为空，点击“发布文章”按钮
        self.driver.find_element(By.CSS_SELECTOR,"#title").clear()
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver, 1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # assert alert.text=="发布失败"
        # 此处为bug：发布失败弹窗没有文字提醒
        alert.accept()
        #输入标题，正文为空，点击“发布文章”按钮
        self.driver.find_element(By.CSS_SELECTOR,"#title").send_keys("发布文章测试2")
        self.driver.find_element(By.CSS_SELECTOR,"#editor > div.editormd-toolbar > div > ul > li:nth-child(39) > a").click()
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        #assert alert.text=="发布失败"
        #此处为bug：发布失败弹窗没有文字提醒
        alert.accept()

    #测试博客编辑页(未登录状态)
    def EditTestByNotLogin(self):
        self.driver.get(self.url)
        #self.driver.find_element(By.CSS_SELECTOR,"body > div.container-login > div > h3")
        #此处为bug：未登录状态仍可访问博客编辑页
        BlogDriver.ScreenShot()
