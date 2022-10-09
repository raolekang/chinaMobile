import time

import pytest
from selenium import webdriver
'''
The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
'''

@pytest.fixture(scope="class")
def manage_brower():
    driver = webdriver.Chrome()
    yield driver
    print("什么时候执行我")
    time.sleep(5)
    driver.quit()