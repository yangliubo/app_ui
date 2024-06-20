from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class StudentAskForLeaveDetailPageElements:
    def __init__(self) -> None:
        self.student_name = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/dayoff_detail_user_tv')
        self.leave_info_items = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/dayoff_item_container_layout')
        self.applicant_info = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("申请人:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.leave_days = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("申请天数:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.start_time = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("开始时间:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.end_time = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("结束时间:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.reason = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("理由:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.status = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("审核状态:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        self.notes = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("备注:").fromParent(resourceId("com.yuanding.seebaby:id/item_dayoff_detail_text"))')
        