#处理每个页面的对象差异
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from production.base.basepage import BasePage
from production.data.read_write_relevance import YamlUtil
from selenium.webdriver import ActionChains

class CreateTemplate(BasePage):

    emptyCreate = (By.XPATH,'//div[@class="emptyCreate"]') #创建新模板
    serviceObject = (By.XPATH,'//span[text()="服务类"]')  #服务类
    neseblod = (By.XPATH,'//div[@class="suite-item-title" and text()="多图文"]/..')  #多图文
    # 第一张 图片
    firstPicture = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div/article/div[4]/img')  #模板大图
    firstSelectFromPictures = (By.XPATH,'//button[@type="button"]/span[text()="从图库选择"]')  #从图库选择
    # 选择审核通过的图片
    firstApprovedImages = (By.XPATH,'//*[@id="app"]/div[1]/div[4]/div/div[2]/div/div[2]/div/ul/li/span[text()="审核通过"]/following-sibling::div[1]')
    #选择图片
    firstSelectPicture = (By.XPATH,'//*[@id="app"]/div[1]/div[4]/div/div[2]/div/div[2]/div/ul/li/span[text()="审核通过"]/following-sibling::div[3]/div[text()="选择图片"]')
    #事件类型
    eventType = (By.XPATH,'//*[@id="app"]/div[1]/aside/section/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/div/div')
    #打开浏览器
    openBrowser = (By.XPATH,'//li/span[text()="打开浏览器"]')
    #定位链接输入框
    linkInputBox = (By.XPATH,'//*[@id="app"]/div[1]/aside/section/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/span')
    # 第二张 图片
    secondPicture= (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div/article/div[5]/img')
    # 从图库选择
    secondSelectFromPictures = (By.XPATH, '//*[@id="app"]/div[1]/aside/section/div[2]/div[1]/div[1]/div[2]/button/span')
    #审核通过的图片
    secondApprovedImages = (By.XPATH,
                      '//*[@id="app"]/div[1]/div[4]/div/div[2]/div/div[2]/div/ul/li/span[text()="审核通过"]/following-sibling::div[1]')
    #选择图片
    secondSelectPicture = (By.XPATH,'//*[@id="app"]/div[1]/div[4]/div/div[2]/div/div[2]/div/ul/li/span[text()="审核通过"]/following-sibling::div[3]/div[text()="选择图片"]')

    #提交按钮
    submitButton = (By.XPATH, '//button/span[text()=" 提交 "]')
    #模板名称
    tmpName = (By.XPATH, '//input[@placeholder="请输入模板名称"]')
    #使用场景
    usageScenario = (By.XPATH, '//input[@placeholder="请输入模板使用场景（如秒杀抢购）"]')
    #模板用途
    # tmpUse = (By.XPATH, '/html/body/div[3]/div/div[2]/form/div[3]/div/div/div/input')
    tmpUse = (By.XPATH, '//input[@placeholder="请选择模板用途"]')
    #测试模板
    testTmp = (By.XPATH, '//li/span[text()="测试模板"]')
    #VIVO复选框
    vivoCheckBox = (By.XPATH, '//input[@value="VIVO"]/..')
    # OPPO复选框
    oppoCheckBox = (By.XPATH, '//input[@value="OPPO"]/..')
    #短信内容
    stringContent = (By.XPATH, '//textarea[@placeholder="请输入短信内容，该内容为发送模板时使用的短信内容"]')
    # 提交审核按钮
    submitCheckButton = (By.XPATH, '//button/span[text()=" 提交审核 "]')
    # 搜索按钮
    searchButton = (By.XPATH, '//span[text()="搜索"]')

    #我的模板，所以模板
    myAllTemplate = (By.XPATH,'//div[@class="descrip"]')

    def create_template(self):
        allhandles = self.driver.window_handles  # 获取当前窗口句柄
        # print('第2次打印窗口',allhandles)
        if self.driver.current_window_handle == allhandles[0]:
            pass
        else:
            self.driver.switch_to.window(allhandles[0])
        #创建新模板
        self.click(self.emptyCreate)
        allhandles = self.driver.window_handles  # 获取当前窗口句柄
        # print('第3次打印窗口', allhandles)
        if self.driver.current_window_handle == allhandles[-1]:
            pass
        else:
            self.driver.switch_to.window(allhandles[-1])
        # window_handles = self.driver.window_handles
        # self.driver.switch_to.window(window_handles[1])  # 切换标签页
        self.click(self.serviceObject)
        self.click(self.neseblod)
        self.click(self.firstPicture)
        self.click(self.firstSelectFromPictures)
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.location(self.firstApprovedImages)).perform() # 鼠标悬浮到图片上
        time.sleep(1)
        # 点击 选择图片
        self.click(self.firstSelectPicture)
        time.sleep(1)
        #点击事件类型
        self.click(self.eventType)
        time.sleep(1)
        #点击打开浏览器
        self.click(self.openBrowser)
        # 点击链接输入框
        time.sleep(1)
        self.click(self.linkInputBox)
        time.sleep(1)
        # div 元素 使用js 脚步修改text 内容
        self.driver.execute_script("document.getElementsByClassName('z-active')[1].innerText='https://www.baidu.com'")
        time.sleep(5)
        #第二张图片
        self.click(self.secondPicture)
        #从图库选择
        self.click(self.secondSelectFromPictures)
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.location(self.secondApprovedImages)).perform()  # 鼠标悬浮到图片上
        time.sleep(1)
        self.click(self.secondSelectPicture)
        time.sleep(1)
        # 点击事件类型
        self.click(self.eventType)
        time.sleep(1)
        # 点击打开浏览器
        self.click(self.openBrowser)
        # 点击链接输入框
        self.click(self.linkInputBox)
        time.sleep(1)
        # div 元素 使用js 脚步修改text 内容
        self.driver.execute_script("document.getElementsByClassName('z-active')[1].innerText='https://www.baidu.com'")
        time.sleep(5)

        # 点击提交按钮
        self.click(self.submitButton)
        # 模板名称
        self.input(self.tmpName,"测试多图文模板")
        # 使用场景
        self.input(self.usageScenario,"测试使用")
        # 模板用途
        self.click(self.tmpUse)
        time.sleep(1)
        # 测试模板
        self.click(self.testTmp)
        try:
            # vivo 复选框
            self.click(self.vivoCheckBox)
            # oppo 复选框
            self.click(self.oppoCheckBox)
        except (NoSuchElementException):
            pass
        # 短信内容
        self.input(self.stringContent,"测试短信示例一")
        # 提交审核按钮
        self.click(self.submitCheckButton)
        time.sleep(1)

        # 创建模板成功 ， 切换窗口至ec
        self.driver.switch_to.window(allhandles[0])
        #点击搜索按钮
        self.click(self.searchButton)
        time.sleep(2)

        # 遍历我的模板
        templates = self.locations(self.myAllTemplate)
        for temp in templates:
            newTplName = temp.find_element(By.XPATH, './child::p[1]').text[3:]
            if newTplName == '测试多图文模板':
                newTplId = temp.find_element(By.XPATH, './child::p[2]').text[3:]
                print("新建模板newTplId:",newTplId)
                YamlUtil.write_append_relevance_yaml(YamlUtil(),data={"newTplId":newTplId})
                # print("value:",value)
            break
