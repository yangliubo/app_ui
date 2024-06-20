import sys
BASE_DIR= 'e:\\python_project\\app_ui'
sys.path.append(BASE_DIR)

from page.index_page import IndexPage
from base.teacher_client import TeacherClient
from page.sign.sign_index_page import SignIndexPage
from page.sign.sign_module.sign_module_index_page import SignModuleIndexPage
from page.sign.sign_module.student_roll_call_mode.student_roll_call_page import StudentRollCallPage
import pytest

@pytest.mark.hehe
class TestSign:
    def setup_class(self):
        self.client = TeacherClient()
        self.operator = self.client.operator
        self.index_page = IndexPage(self.client)
        # self.index_page.goto_sign_module()
        self.sign_index_page = SignIndexPage(self.client,is_init_to_page=False)
        # self.sign_index_page.goto_sign_module()
        self.sign_module_index_page = SignModuleIndexPage(self.client,is_init_to_page=False)
        # self.sign_module_index_page.go_to_student_roll_call_page()
        
        self.stu_roll_call_page = StudentRollCallPage(self.client)
        
        
    # def teardown_method(self):
    #     self.operator.start_activity('com.yuanding.seebaby','com.yuanding.seebaby.WelcomeActivity')
    #     self.index_page.goto_sign()
    #     self.sign_index_page.goto_sign_module()
    #     self.sign_module_index_page.go_to_student_roll_call_page()
        
        
        
    def test_sign_in_student_by_hand(self):
        # 跳过引导
        self.stu_roll_call_page.skip_guide_page()
         # 获取已签到、未签到的人数
        dic = self.stu_roll_call_page.get_sign_and_unsigned_students_num()
        # 给学生手动签到
        name_sign = self.stu_roll_call_page.sign_first_unsigned_student()
        # 点名后获取已签到、未签到的人数
        dic1 = self.stu_roll_call_page.get_sign_and_unsigned_students_num()
        assert dic1['sign_count'] == dic['sign_count']+1
        # 切换到已签到tab
        self.stu_roll_call_page.switch_to_signed_tab()
        name_set = self.stu_roll_call_page.get_all_name_under_the_tab()
        # 校验已签到列表包含刚刚签到的人
        assert name_sign in  name_set
        # # 切换到签退模式
        # self.stu_roll_call_page.switch_sign_mode()
        # # 获取可签退的名单
        # name_set_can_be_signed_out = self.stu_roll_call_page.get_all_name_under_the_tab()
        # assert name_sign in name_set_can_be_signed_out
        # # 签退
        # name_signed_out = self.stu_roll_call_page.sign_first_no_sign_out_student()
        # # 切换到已签退列表，判断人员在列表中
        # self.stu_roll_call_page.switch_to_signed_tab()
        # name_set_signed_out = self.stu_roll_call_page.get_all_name_under_the_tab()
        # assert name_signed_out in name_set_signed_out
        # self.stu_roll_call_page.back_to_superior_page()
        # lastest_sign_name = self.sign_module_index_page.get_sign_person_name()
        # second_sign_name = self.sign_module_index_page.get_sign_person_name(1)
        # assert lastest_sign_name in  lastest_sign_name
        # assert name_signed_out in second_sign_name
        
        
    # def test_sign_out_student_by_hand(self):
    #     name_sign = self.stu_roll_call_page.sign_first_unsigned_student()

    #     assert name_sign in name_set
        
        