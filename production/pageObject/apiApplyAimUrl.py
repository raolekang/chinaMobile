'''
    申请短链
'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from production.base.basepage import BasePage
from production.data.read_write_relevance import YamlUtil


class ApiApplyAimUrl(BasePage,YamlUtil):

    # 模板id输入框
    tempId = (By.XPATH, '//input[@placeholder="请输入模板ID查询"]')
    # 搜索按钮
    searchButton = (By.XPATH, '//span[text()="搜索"]')
    # 卡片对象
    card = (By.XPATH, '//div[@class="previewClass"]')
    # 短链生成
    ulrApply = (By.XPATH, '//div[@class="boxCenter"]/div[text()="短链生成"]')
    # 最大解析次数
    maxShowTimes = (By.XPATH, '//input[@placeholder="请输入生成短链的最大可解析次数，最多10000000（单位：次）"]')
    # 短信签名
    msgSignature = (By.XPATH, '//input[@placeholder="请输入短信签名，注意不能输入【】"]')
    # 确认信息无误按钮
    checkbox = (By.XPATH, '//label[@class="el-checkbox"]')
    # 生成短链按钮
    applyUrlFirstButton = (By.XPATH, '//button/span[text()="生成短链"]')
    # 短链生成第二步，确认按钮
    applyUrlSecondButton = (By.XPATH, '//button[@type="button" and contains(@class,"next-btn")]/span[text()="确定"]')
    # 短链生成第二步，继续生成按钮
    ContinueApplyButton = (By.XPATH, '//button/span[contains(text(),"继续生成")]')
    # 生成的短链
    aimUrl = (By.XPATH, '//div[@class="flex-title" and text()="短链链接："]/following-sibling::div[1]')
    # 关闭页面按钮
    closeButton = (By.XPATH, '//span[text()="短链生成"]/following-sibling::button[@aria-label="Close" and @class="el-dialog__headerbtn"]')

    # 通知王地址
    noticeWang = "https://con.5itz.cn:9609/tzwc/acc/acc_login.html"
    # 账号密码登录按钮
    accountPwdBtn = (By.XPATH, '//button[text()="账号密码登录"]')
    # 用户名
    username = (By.XPATH, '//input[@id="username"]')
    # 密码
    password = (By.XPATH, '//input[@id="password"]')
    # 登录按钮
    loginBtn = (By.XPATH, '//input[@class="btn"]')
    # 短信按钮
    msgBtn = (By.XPATH, '//img[@src="../frame/images/notice-icon6.png"]')
    # 短信内容编辑文本域
    msgTextarea = (By.XPATH, '//textarea[@id="qc-cont1"]')
    # 接收人员
    receiveMan = (By.XPATH, '//div[@id="qcMet"]/*/*/*/*/ul[contains(@class,"js-normal-op")]/li[@class="add-per"]')
    # 手动录入
    manually = (By.XPATH, '//li[text()="手动录入"]')
    # 输入成员信息输入框
    membershipTextarea = (By.XPATH, '//textarea[@name="userphone"]')
    # 添加按钮
    addBtn = (By.XPATH, '//button[contains(@class,"js-manual-add")]')
    # 确定按钮
    confirmBtn = (By.XPATH, '//button[@id="add-group_members"]')
    # 发送按钮
    sendBtn = (By.XPATH, '//button[text()="暂存"]/following-sibling::button[contains(@class,"qcSent")]')
    # 最后的确认发送按钮
    lastConfirBtn = (By.XPATH, '//div[@id="qcSend-sure"]/div/div/div[3]/button[1]')


    def apiApplyAimUrl(self,templayeId):
        # 获取当前窗口句柄
        allhandles = self.driver.window_handles
        if self.driver.current_window_handle == allhandles[0]:
            pass
        else:
            self.driver.switch_to.window(allhandles[0])
        self.input(self.tempId,templayeId)
        self.click(self.searchButton)
        # 鼠标悬浮至申请短链上
        ActionChains(self.driver).move_to_element(self.location(self.card)).perform()  # 鼠标悬浮到图片上
        time.sleep(2)
        self.click(self.ulrApply)
        self.input(self.maxShowTimes,10)
        self.input(self.msgSignature,"通知王")
        self.click(self.checkbox)
        time.sleep(1)
        self.click(self.applyUrlFirstButton)
        time.sleep(1)
        print("----------------------------------------------------")
        self.click(self.applyUrlSecondButton)
        time.sleep(1)
        self.click(self.ContinueApplyButton)
        time.sleep(1)
        # 获取短链
        aimUrl = (self.location(self.aimUrl).text).strip()
        print("生成的短链",aimUrl)
        try:
            YamlUtil.read_relevance_yaml(YamlUtil(), "aimUrl")
        except(KeyError):
            YamlUtil.write_append_relevance_yaml(YamlUtil(), {"aimUrl": aimUrl})
        self.click(self.closeButton)
        # 打开通知王
        js = f'window.open("{self.noticeWang}")'
        self.driver.execute_script(js)
        time.sleep(1)
        # 切换窗口
        allhandles = self.driver.window_handles
        if self.driver.current_window_handle == allhandles[-1]:
            pass
        else:
            self.driver.switch_to.window(allhandles[-1])
        self.click(self.accountPwdBtn)
        self.input(self.username,"18718816544")
        self.input(self.password,"Llh123456")
        self.click(self.loginBtn)
        time.sleep(5)
        self.click(self.msgBtn)
        # 要输入的短信内容
        # msgText = "测试："+"zyaim.y0k.cn/qyS16f"
        msgText = "测试："+YamlUtil.read_relevance_yaml(YamlUtil(),"aimUrl")
        self.input(self.msgTextarea,msgText)
        time.sleep(1)
        self.click(self.receiveMan)
        time.sleep(1)
        # 手动录入
        self.click(self.manually)
        # 输入手机号码
        self.input(self.membershipTextarea,"13979548340")
        time.sleep(1)
        self.click(self.addBtn)
        time.sleep(1)
        self.click(self.confirmBtn)
        time.sleep(2)
        self.click(self.sendBtn)
        time.sleep(3)
        #  cls.driver.find_element().screenshot("确认发送.png")
        # self.location(self.lastConfirBtn).screenshot("确认发送.png")
        #  cls.driver.find_element().get_attribute("outerHTML")
        # print("元素标签内容 ------》",self.location(self.lastConfirBtn).get_attribute("outerHTML"))
        self.click(self.lastConfirBtn)
        time.sleep(3)
        self.driver.close()
        time.sleep(3)






