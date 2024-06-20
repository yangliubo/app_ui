from appium.webdriver.common.mobileby import MobileBy
from common.element_info import ElementInfo
from selenium.webdriver.support import expected_conditions as EC

class AskForLeaveForStudentElements:
    def __init__(self) -> None:
        self.title = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_center')
        # 时间标签--上午、下午、全、今天、多天
        self.time_tag_morning = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='上午')
        self.time_tag_aftertnoon = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='下午')
        self.time_tag_all_day = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='今天')
        self.time_tag_several_day = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='多天')
        # 请假标签--病假、事假、感冒、发烧、腹泻、水痘、手足口、腮腺炎、其他
        self.leave_tag_sick = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='病假')
        self.leave_tag_business = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='事假')       
        # 生病标签
        self.sick_tag_cold = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='感冒')       
        self.sick_tag_fever = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='发烧')       
        self.sick_tag_diarrhea = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='腹泻')       
        self.sick_tag_chickenpox = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='水痘')
        self.sick_tag_hfmd = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='手足口')       
        self.sick_tag_mumps = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='腮腺炎')       
        self.sick_tag_others = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_tag',expect_condition='text_in_elements',expect_value='其他')       
        # 输入框--请假原因
        self.apply_reason = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/et_apply_reason')
        # 上传照片按钮
        self.upload_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/iv_picture')
        # 弹窗同意按钮
        self.agree_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_agree',timeout=3)
        # 弹窗拒绝按钮
        self.reject_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_agree')
        # 拍照按钮
        self.take_photo_btn = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("拍照")')
        # 从手机相册选择按钮
        self.choose_photo_from_phone_btn = ElementInfo(locator_type=MobileBy.ANDROID_UIAUTOMATOR,locator_value='new UiSelector().text("从手机相册选择")')
        # 系统相册选择按钮 
        self.choose_photo_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/layout_cb_check')
        # 系统相册选择完成按钮
        self.sys_album_finish_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/tv_right')
        # 提交按钮
        self.submit_btn = ElementInfo(locator_type=MobileBy.ID,locator_value='com.yuanding.seebaby:id/btn_submit')