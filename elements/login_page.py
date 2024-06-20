from common.element_info import ElementInfo
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
class LoginPageElements:
    def __init__(self) -> None:
        self.privacy_agreement_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_agree')
        self.buttom_sliding_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/indicator')
        self.experience_btn = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("立即体验")')
        self.login_by_account_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_login_other_way')
        self.account_input = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/phoneNum')
        self.passwd_input = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/authCode')
        self.login_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/login')
        self.agree_deal_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/iv_check_protocol')
        
        