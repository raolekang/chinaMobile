'''
模板审核、激活
'''
import time

from selenium.webdriver.common.by import By

from production.base.basepage import BasePage
class TemplateCheckActive(BasePage):
    # 模板id 输入框
    templateId = (By.XPATH,'//input[@placeholder="请输入模板ID查询"]')
    # 搜索按钮
    searchButton = (By.XPATH,'//button/span[text()="搜索"]')
    # 审核按钮
    checkButton = (By.XPATH,'/html/body/section/section/main/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr/td[12]/div/div/span[2]')
    # 全部通过
    allPassButton = (By.XPATH,'//span[text()="全部通过"]/..')
    # 审核意见
    textarea = (By.XPATH,'//textarea')
    # 同步至厂商 华为 ：
    huaweiCheckBox = (By.XPATH,'//label[text()="同步到厂商:"]/following-sibling::div[1]/div[1]/label[1]/span[text()="HuaWei"]/..')
    # 同步至厂商 小米
    xiaomiCheckBox = (By.XPATH,'//label[text()="同步到厂商:"]/following-sibling::div[1]/div[1]/label[2]/span[text()="XiaoMi"]/..')
    # 确认审核按钮
    affirmCheckButton = (By.XPATH, '//button/span[text()="确认审核"]')

    # 模板状态管理
    templateStatusManagement = (By.XPATH, '//span[@class="muen2" and text()="模板状态管理"]')
    # 激活
    activeButton = (By.XPATH, '/html/body/section/section/main/div/div/div[1]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td[17]/div/div/span[3]')
    # 全选
    selectAll = (By.XPATH, '/html/body/section/section/main/div/div/div[2]/div/div[2]/form/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label')
    # 审核意见
    checkOpinion = (By.XPATH, '//textarea')
    # 提交按钮
    submitButton = (By.XPATH, '//button/span[text()="提 交"]')

    def tmpCheckActive(self,tmpId):
        allhandles = self.driver.window_handles  # 获取当前窗口句柄
        if self.driver.current_window_handle == allhandles[0]:
            pass
        else:
            self.driver.switch_to.window(allhandles[0]) #切换到运营平台
        self.input(self.templateId,tmpId)
        self.click(self.searchButton)
        self.click(self.checkButton)
        time.sleep(1)
        # 鼠标滚动到底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        self.click(self.allPassButton)
        self.input(self.textarea,"审核通过")
        self.click(self.huaweiCheckBox)
        self.click(self.xiaomiCheckBox)
        self.click(self.affirmCheckButton)
        # 审核完成，开始激活
        time.sleep(1)
        self.click(self.templateStatusManagement)
        self.input(self.templateId, tmpId)
        time.sleep(1)
        self.click(self.searchButton)
        time.sleep(2)
        # 继续点击搜索
        self.click(self.searchButton)
        time.sleep(2)
        self.click(self.activeButton)
        time.sleep(2)
        self.click(self.selectAll)
        self.input(self.checkOpinion,"审核意见：通过")
        time.sleep(1)
        self.click(self.submitButton)
        time.sleep(1)
        # 再激活一遍，防止有厂商未刷新出来
        self.click(self.searchButton)
        time.sleep(2)
        self.click(self.activeButton)
        time.sleep(1)
        self.click(self.selectAll)
        time.sleep(1)
        self.click(self.submitButton)


