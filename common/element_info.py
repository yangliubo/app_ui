
from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait
class ElementInfo:
    def __init__(self,locator_type:MobileBy,locator_value:str,timeout:int=30,expect_condition=None,poll_frequency:float=0.5,expect_value:str=None) -> None:
        self.locator_type = locator_type
        self.locator_value = locator_value
        self.timeout = timeout
        self.expect_condition = expect_condition
        self.poll_frequency = poll_frequency
        self.expect_value = expect_value