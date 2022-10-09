import os

import yaml
'''
print(os.getcwd())
        print(os.getcwd().find("testing"))
        # testing 所在下标
        index = os.getcwd().find("testing")
'''

class YamlUtil:
    # 截取testing前面部分
    path = os.getcwd()[:os.getcwd().find("testing")]

    # 读取文件中的数据
    def read_relevance_yaml(self,key):
        print("读文件的路径：",self.path+r'testing\data\relevance.yaml')
        with open(self.path+r'testing\data\relevance.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader) # 读取文件内容，返回字典
            return value[key]

    # 写入 relevance.yaml 文件数据  mode='w' : 先清空文件内容 ，然后写入
    def write_relevance_yaml(self, data):
        print("写入文件的路径：",self.path+r'testing\data\relevance.yaml')
        with open(self.path+r'testing\data\relevance.yaml', mode='w', encoding='utf-8') as f:
            value = yaml.dump(stream=f, data=data, allow_unicode=True)  # 写入文件数据 ，data 为字典
            return value

    # 写入 relevance.yaml 文件数据  mode='a' : 不清空文件内容 ，追加写入
    def write_append_relevance_yaml(self, data):
        print("写入文件的路径：", self.path + r'testing\data\relevance.yaml')
        with open(self.path+r'testing\data\relevance.yaml', mode='a', encoding='utf-8') as f:
            value = yaml.dump(stream=f, data=data, allow_unicode=True)  # 写入文件数据 ，data 为字典
            return value

if __name__ == '__main__':
    YamlUtil().read_relevance_yaml(key="newTplId")