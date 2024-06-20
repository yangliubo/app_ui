from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class SignIndexPageElements:
    def __init__(self) -> None:
        self.count_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab',expect_condition='text_in_elements',expect_value='统计')
        self.sign_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab',expect_condition='text_in_elements',expect_value='签到')
        self.setting_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab',expect_condition='text_in_elements',expect_value='设置')
        self.back_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/img_back')

        