#处理每个页面的对象差异
import time
from selenium.webdriver.common.by import By
from testing.base.basepage import BasePage


class SearchTemplate(BasePage):

    tempId = (By.XPATH,'//input[@placeholder="请输入模板ID查询"]') #模板id输入框
    searchButton = (By.XPATH,'//span[text()="搜索"]')  #搜索按钮


    def search_template(self,tempId):
        self.input(self.tempId,tempId)
        time.sleep(2)
        self.click(self.searchButton)





