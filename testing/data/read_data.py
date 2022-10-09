import yaml


class ReadYaml:

    def readYamlFile(self,file):
        with open(file,mode='r',encoding='utf-8') as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            print(data)
            return data
