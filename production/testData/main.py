import os
import pytest

if __name__ == '__main__':
    '''
        --alluredir :生成测试数据
        ./report/result : 生成测试数据目录
        --alluredir=./report/result :生成临时文件路径
        test_dxweb02.py :要执行的用例文件
    '''
    pytest.main(["--alluredir=./report/result",'../testCases/test_dxweb.py'])
    # 命令行执行  test_allure serve allure结果文件路径
    # 或者
    os.system("allure generate --clean ./report/result -o ./report/html/")

