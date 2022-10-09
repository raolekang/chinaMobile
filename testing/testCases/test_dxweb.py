import os
import sys


# 以下方法可以实现在终端运行python文件r
sys.path.append(os.getcwd()[:os.getcwd().find("chinaMobile")+11])
from testing.pageObject.apiApplyAimUrl import ApiApplyAimUrl
from testing.pageObject.login import Login
from testing.pageObject.searchTemplate import SearchTemplate
from testing.pageObject.createTemplate import CreateTemplate
from testing.pageObject.tmpCheckAndActive import TemplateCheckActive
from testing.data.read_write_relevance import  YamlUtil
import pytest
from testing.data.read_data import ReadYaml

class Testtesting:

    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #
    # def teardown_class(self):
    #     self.driver.quit()

    #登录EC/OS
    @pytest.mark.parametrize("data",ReadYaml().readYamlFile(file=os.getcwd()[:os.getcwd().find("testing")]+r'testing\data\data.yaml'))
    def test_login(self,data,manage_brower):
        print("登录时读取配置文件路径：",os.getcwd()[:os.getcwd().find("testing")]+r'testing\data\data.yaml')
        self.loginPage = Login(driver=manage_brower)
        self.loginPage.login(ecUrl=data["ecUrl"],ecUserName=data["ecAccount"], ecPassWord=data["ecPwd"],osUrl=data["osUrl"], osUserName=data["osAccount"], osPassWord=data["osPwd"])
        assert  "cszh0120" in self.loginPage.getAssertValue()


    #创建模板
    def test_createTemplate(self,manage_brower):
        createTemp= CreateTemplate(driver=manage_brower)
        createTemp.create_template()

    # 查询模板
    def test_searchTemplate(self,manage_brower):
        # print("读取relevance.yaml文件中的数据",newTplId)
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId") #使用封装的方法读取
        searchTempObject = SearchTemplate(driver=manage_brower)
        searchTempObject.search_template(tmpId)

    #模板审核激活
    def test_templateCheckActive(self,manage_brower):
        tmpCheckActive = TemplateCheckActive(driver=manage_brower)
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        tmpCheckActive.tmpCheckActive(tmpId=tmpId)

    # 申请短链
    def test_apiApplyAimUrl(self,manage_brower):
        templateId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        print("templateId:", templateId)
        apiApplyAimUrl = ApiApplyAimUrl(driver=manage_brower)
        apiApplyAimUrl.apiApplyAimUrl(templateId)

if __name__ == '__main__':
    pytest.main(['-vs'])
