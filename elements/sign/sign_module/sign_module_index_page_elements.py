from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class IndexPageElements:
    def __init__(self) -> None:
        # 学生签到tab
        self.student_tab = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab_title',expect_condition='text_in_elements',expect_value='学生签到')
        # 老师签到tab
        self.teacher_tab = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tab_title',expect_condition='text_in_elements',expect_value='老师签到')
        # 签到记录/月度统计
        self.sign_record_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvRecord')
        # 学生点名/老师点名
        self.roll_call_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvAttendance')
        # 代接确认
        self.pick_up_confirm_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvShuttle') 
        # 我的签到
        self.my_sign_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvSign')
        # 签到列表--签到人姓名
        self.sign_name = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvBabyName')
        # 签到列表--备注
        self.remark = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tvDes')
        
        