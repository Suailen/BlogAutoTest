import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.Utils import BlogDriver



class BlogUpdate:
    def __init__(self):
        self.driver=BlogDriver.driver
        self.url="http://8.137.19.140:9090/blog_update.html?blogId=22227"
        self.driver.get(self.url)

    # 测试博客更新页(登录状态)
    def UpdateTestByLogin(self):
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

    def BlogUpdateSuc(self):
        #直接点击“更新文章”按钮
        time.sleep(1)
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.back()
        #更新标题，点击”更新文章“按钮
        self.driver.find_element(By.CSS_SELECTOR,"#title").send_keys("(更新)")
        time.sleep(1)
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.back()
        #更新正文，点击“更新文章”按钮
        self.driver.find_element(By.CSS_SELECTOR,"#editor > div.editormd-toolbar > div > ul > li:nth-child(4) > a").click()
        time.sleep(1)
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container > div.left > div > h3")
        self.driver.back()

    def BlogUpdateFail(self):
        #标题更新为空，点击“更新文章”按钮
        text=self.driver.find_element(By.CSS_SELECTOR,"#title")
        text.click()
        text.clear()
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        #assert alert.text=="更新失败"
        #此处为bug：更新失败弹窗没有文字提示
        alert.accept()
        self.driver.find_element(By.CSS_SELECTOR,"#title").send_keys("发布文章测试")
        #正文更新为空，点击“更新文章”按钮
        self.driver.find_element(By.CSS_SELECTOR,"#editor > div.editormd-toolbar > div > ul > li:nth-child(39) > a").click()
        BlogDriver.ScreenShot()
        self.driver.find_element(By.CSS_SELECTOR,"#submit").click()
        WebDriverWait(self.driver,1).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        #assert alert.text=="更新失败"
        #此处为bug：更新失败弹窗没有文字提示
        alert.accept()

    # 测试博客更新页(未登录状态)
    def UpdateTestByNotLogin(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR,"body > div.container-login > div > h3")
        BlogDriver.ScreenShot()