from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class StudentTemperatureCountPageElements:
    def __init__(self) -> None:
        self.rows = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.collect-title')
        self.class_name = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.title-name.spn.c33')
        self.normal_count = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.title-normal.spn')
        self.hot_count = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.title-hot.spn')
        self.not_test_count = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.title-not.spn')
        self.refresh_btn = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="van-toast van-toast--middle van-toast--loading"]',timeout=3)
        self.list_zone = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.collect-list')
        self.list_zone_native = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/viewPager')
        self.back_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/img_back')