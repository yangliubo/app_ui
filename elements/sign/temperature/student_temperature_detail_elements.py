from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class StudentTemperatureDetailElements:
    def __init__(self) -> None:
        self.tab_normal = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="spn" and contains(text(),"正常")]')
        self.tab_fever = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="spn" and contains(text(),"发热")]')
        self.tab_untested = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="spn" and contains(text(),"未检测")]')
        self.fill_in_temperature_btns = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.entry-btn.c0a')
        self.names = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.lt-name')
        self.commit_btn = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="btn-sum van-button van-button--info van-button--normal van-button--round"]')
        self.cancel_btn = ElementInfo(locator_type=MobileBy.XPATH,locator_value='//*[@class="btn-end van-button van-button--default van-button--normal van-button--round"]')
        self.add_btn = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.van-stepper__plus')
        self.subtract_btn = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.van-stepper__minus')
        self.temperature_input = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.van-stepper__input')
        self.status = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.cf9')
        self.temperature = ElementInfo(locator_type=MobileBy.CSS_SELECTOR,locator_value='.lt-content-value')
        self.back_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/iv_back')