from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions 
from common.element_info import ElementInfo

class StudentRollCallElements:
    def __init__(self) -> None:
        # 返回按钮
        self.back_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/ib_left')
        # 引导页面
        self.guide_page = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/rl_root',timeout=3)
        # 引导按钮--我知道了
        self.guide_know_more_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/iv_guide_3')
        # 签到签退切换按钮
        self.sign_switch_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_right')
        # 选择班级按钮
        self.classes_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_center')
        # 学生列表
        self.student_row = ElementInfo(locator_type=MobileBy.ID,locator_value='roll_call_item')
        # 学生姓名
        self.student_name = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/name')
        # 签到状态
        self.student_sign_status = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/checkbox')
        # 请假状态
        self.student_leave_status = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/leave')
        # 标题tab 
        self.tab = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab_title')
        # 列表区域
        self.list_zone = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/viewPager')
        # 横幅--请假信息
        self.tip_ask_for_leave_info = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/leave_checkbox')
        # 页面刷新中按钮
        self.refresh_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/srl_classics_title')
        
    def _get_status_value_by_student_name(self,name):
        '''根据姓名获取请假状态的 locator_value'''
        value = 'new UiSelector().text("%s").fromParent(resourceId("com.yuanding.seebaby:id/leave"))'%(name)
        return value
    
    def generator_sutdent_status_element(self,name):
        '''根据姓名获取 请假状态的元素'''
        value = self._get_status_value_by_student_name(name)
        print('元素是:',value)
        student_sign_status = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value=value,timeout=5)
        return student_sign_status