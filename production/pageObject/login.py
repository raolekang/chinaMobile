#处理每个页面的对象差异
import time
from selenium.webdriver.common.by import By
from production.base.basepage import BasePage
from selenium import webdriver
class Login(BasePage):

    # 客户平台
    ecPassLogin = (By.XPATH,'//div[text()="密码登录"]') # 密码登录
    ecUserName = (By.XPATH,'//input[@placeholder="请输入用户名"]')
    ecPassWord = (By.XPATH,'//input[@placeholder="请输入密码"]')
    ecButton = (By.XPATH,'//button/span[text()="登录"]')
    #运营平台
    osPassLogin = (By.XPATH, '//div[text()="密码登录"]')  # 密码登录
    osUserName = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    osPassWord = (By.XPATH, '//input[@placeholder="请输入密码"]')
    osButton = (By.XPATH, '//button/span[text()="登录"]')

    #定位要断言的元素
    loginAccount = (By.XPATH, '//img[@src="static/img/icon_wode.3c1a0d82.png"]/..')

    def loginEc(self,ecUrl,ecUserName,ecPassWord):
        self.load_url(ecUrl)
        self.click(loc=self.ecPassLogin)
        self.input(self.ecUserName,ecUserName)
        self.input(self.ecPassWord,ecPassWord)
        time.sleep(6)
        self.click(loc=self.ecButton)
        time.sleep(5)

    def loginOs(self,  osUrl, osUserName, osPassWord):
        self.load_url(osUrl)
        self.click(loc=self.ecPassLogin)
        self.input(self.osUserName, osUserName)
        self.input(self.osPassWord, osPassWord)
        time.sleep(6)
        self.click(loc=self.osButton)
        time.sleep(5)

    def getAssertValueEc(self):
        return self.location(loc=(By.XPATH, '//img[@src="static/img/icon_wode.3c1a0d82.png"]/..')).get_attribute(
            'textContent')

    def getAssertValueOs(self):
        return self.location(loc=(By.XPATH, '//i[@class="el-icon-user"]/..')).get_attribute('textContent')
