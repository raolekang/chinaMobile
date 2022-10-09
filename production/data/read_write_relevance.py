import os

import yaml



class YamlUtil:

    # 读取文件中的数据  print(os.getcwd()) D:\test\pythonProject\企业
    def read_relevance_yaml(self,key):
        with open('../data/relevance.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader) # 读取文件内容，返回字典
            return value[key]

    # 写入 relevance.yaml 文件数据  mode='w' : 先清空文件内容 ，然后写入
    def write_relevance_yaml(self, data):
        with open('../data/relevance.yaml', mode='w', encoding='utf-8') as f:
            value = yaml.dump(stream=f, data=data, allow_unicode=True)  # 写入文件数据 ，data 为字典
            return value

    # 写入 relevance.yaml 文件数据  mode='a' : 不清空文件内容 ，追加写入
    def write_append_relevance_yaml(self, data):
        with open('../data/relevance.yaml', mode='a', encoding='utf-8') as f:
            value = yaml.dump(stream=f, data=data, allow_unicode=True)  # 写入文件数据 ，data 为字典
            return value