import datetime
import os.path
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self):
        options=webdriver.ChromeOptions()
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        self.driver.implicitly_wait(3)

    def ScreenShot(self):
        #创建文件夹
        dir_path="../images/"+datetime.datetime.now().strftime("%Y-%m-%d")
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        #创建屏幕截图
        filename=sys._getframe().f_back.f_code.co_name+'-'+datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")+".png"
        self.driver.save_screenshot(dir_path+'/'+filename)

BlogDriver=Driver()