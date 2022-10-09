import time

import pytest
from selenium import webdriver
'''
The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
'''


@pytest.fixture(scope="class")
def driverEC():
    driver = webdriver.Chrome()
    yield driver
    print("什么时候执行我EC")
    time.sleep(5)
    driver.quit()


@pytest.fixture(scope="class")
def driverOS():
    driver = webdriver.Chrome()
    yield driver
    print("什么时候执行我OS")
    time.sleep(5)
    driver.quit()