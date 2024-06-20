from common.element_info import ElementInfo
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
class IndexPageElements:
    def __init__(self) -> None:	
        self.modules_swip_zone = ElementInfo(locator_type=MobileBy.ID,locator_value="com.yuanding.seebaby:id/rv_model_list")
        self.modules = ElementInfo(locator_type=MobileBy.ID,locator_value="com.yuanding.seebaby:id/tv_title")
        self.sign_module = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("签到")',expect_condition='element_to_be_clickable')
        self.sign_module1 = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("签到")')
        self.publish_btn = ElementInfo(locator_type=MobileBy.ID,locator_value="com.yuanding.seebaby:id/main_tab_publish_icon_iv")