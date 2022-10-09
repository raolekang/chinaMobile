# 页面的基础层 ，处理每个web页面的共性
import time


class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    #封装动作，打开浏览器
    # def open_browser(self,browser):
    #     browser = browser.capitalize() #首字母大小
    #     self.driver = getattr(webdriver,browser)() # 相当于 webdriver.Browser()
    #     self.driver.implicitly_wait(5) #隐式等待

    # 加载地址
    def load_url(self,url):
        self.driver.get(url)

    #定位元素
    def location(self,loc):
        return self.driver.find_element(*loc) # 加*，去掉元组两边的括号

    # 定位多个元素
    def locations(self, loc):
        return self.driver.find_elements(*loc)  # 加*，去掉元组两边的括号

    #输入操作
    def input(self,loc,value):
        self.location(loc).clear() #先清空输入框中的内容
        self.location(loc).send_keys(value)

    #点击操作
    def click(self,loc):
        self.location(loc).click()



