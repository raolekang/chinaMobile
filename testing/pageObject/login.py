#处理每个页面的对象差异
import time
from selenium.webdriver.common.by import By
from testing.base.basepage import BasePage


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

    def login(self,ecUrl,ecUserName,ecPassWord,osUrl,osUserName,osPassWord):
        self.load_url(ecUrl)
        self.click(loc=self.ecPassLogin)
        self.input(self.ecUserName,ecUserName)
        self.input(self.ecPassWord,ecPassWord)
        time.sleep(6)
        self.click(loc=self.ecButton)
        time.sleep(5)
        # 开启一个新的窗口
        js = f'window.open("{osUrl}")'
        self.driver.execute_script(js)
        allhandles = self.driver.window_handles  # 获取当前窗口句柄
        # print('第1次打印窗口', allhandles)
        if self.driver.current_window_handle == allhandles[1]:
            pass
        else:
            self.driver.switch_to.window(allhandles[1])  # 切换窗口 ，切到运营平台
            self.click(loc=self.osPassLogin)
            self.input(self.osUserName, osUserName)
            self.input(self.osPassWord, osPassWord)
            time.sleep(6)
            self.click(loc=self.osButton)
        #切换到客户平台
        self.driver.switch_to.window(allhandles[0])
        time.sleep(2)
    def getAssertValue(self):
        return self.location(loc=(By.XPATH, '//img[@src="static/img/icon_wode.3c1a0d82.png"]/..')).get_attribute('textContent')




