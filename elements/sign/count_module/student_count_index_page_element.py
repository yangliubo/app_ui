from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class StudentCountIndexPageElement:
    def __init__(self):
        # 体温检测卡片
        self.temperature_count_card = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().resourceId("com.yuanding.seebaby:id/statistics_title").text("体温检测")')
        # 体温正常人数 早中晚
        self.temperature_count_normal_counts = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_normal_number')
        # 体温发热人数 早中晚
        self.temperature_count_fever_counts = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_fever_number')
        # 体温未检测人数 早中晚
        self.temperature_count_notest_counts = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_no_detect_number')
        # 