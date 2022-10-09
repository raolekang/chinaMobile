import os
import sys

# 以下方法可以实现在终端运行python文件  sys.path.append(r'D:\test\chinaMobile')
sys.path.append(os.getcwd()[:os.getcwd().find("chinaMobile")+11])
from production.pageObject.apiApplyAimUrl import ApiApplyAimUrl
from production.pageObject.login import Login
from production.pageObject.searchTemplate import SearchTemplate
from production.pageObject.createTemplate import CreateTemplate
from production.pageObject.tmpCheckAndActive import TemplateCheckActive
from production.data.read_write_relevance import  YamlUtil
import pytest
from production.data.read_data import ReadYaml

class Testproduction():

    # def setup_class(self):
    #     self.driverEc = webdriver.Chrome()
    #     self.driverOs = webdriver.Chrome()
    #
    # def teardown_class(self):
    #     self.driverEc.quit()
    #     self.driverOs.quit()

    # 登录EC
    @pytest.mark.parametrize("data", ReadYaml().readYamlFile(file='../data/data.yaml'))
    def test_login(self, data,driverEC,driverOS):
        self.loginPage = Login(driver=driverEC)
        self.loginPage.loginEc(ecUrl=data["ecUrl"], ecUserName=data["ecAccount"], ecPassWord=data["ecPwd"])
        assert data["ecAccount"] in self.loginPage.getAssertValueEc()
        self.loginPage = Login(driver=driverOS)
        self.loginPage.loginOs(osUrl=data["osUrl"], osUserName=data["osAccount"], osPassWord=data["ecPwd"])
        assert data["osAccount"] in self.loginPage.getAssertValueOs()

    #创建模板
    def test_createTemplate(self,driverEC):
        createTemp= CreateTemplate(driver=driverEC)
        createTemp.create_template()

    # 查询模板
    def test_searchTemplate(self,driverEC):
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId") #使用封装的方法读取
        searchTempObject = SearchTemplate(driver=driverEC)
        searchTempObject.search_template(tmpId)

    #模板审核激活
    def test_templateCheckActive(self,driverOS):
        tmpCheckActive = TemplateCheckActive(driver=driverOS)
        tmpId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        tmpCheckActive.tmpCheckActive(tmpId=tmpId)

    # 申请短链
    def test_apiApplyAimUrl(self,driverEC):
        templateId = YamlUtil.read_relevance_yaml(YamlUtil(), "newTplId")
        print("templateId:", templateId)
        apiApplyAimUrl = ApiApplyAimUrl(driver=driverEC)
        apiApplyAimUrl.apiApplyAimUrl(templateId)


if __name__ == '__main__':
    pytest.main(['-vs'])
