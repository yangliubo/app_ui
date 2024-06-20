from page.sign.sign_module.student_roll_call_mode.student_ask_for_leave_page import StudentAskForLeavePage
from page.sign.sign_module.student_roll_call_mode.student_roll_call_page import StudentRollCallPage
from page.sign.sign_module.student_roll_call_mode.student_ask_for_leave_detail_page import StudentAskForLeaveDetailPage
from base.teacher_client import TeacherClient
import pytest
import time
@pytest.mark.gg
class TestTakingLeaveForStudent:
    def setup_class(self):
        self.client = TeacherClient()
        self.roll_call_page = StudentRollCallPage(self.client)
        self.student_leave_detail_page = StudentAskForLeaveDetailPage(self.client)
        self.roll_call_page.waiting_the_page_refresh()
        self.ask_for_leave_count = self.roll_call_page.get_ask_for_leave_count()
        self.student_info = self.roll_call_page.ask_for_leave_for_first_student()
        self.name = self.student_info['name']
        self.ask_for_leave_page = StudentAskForLeavePage(self.client)
        
    def test_submit_ask_for_leave_record(self):
        self.ask_for_leave_page.select_leave_time(1)
        # self.ask_for_leave_page.chose_reason_for_leave()
        self.ask_for_leave_page.chose_sick_type(6)
        self.ask_for_leave_page.fill_in_the_presentation_of_condition('6666')
        self.ask_for_leave_page.choose_picture()
        self.ask_for_leave_page.submit_record()
        self.roll_call_page.click_tips_leave_info()
        self.roll_call_page.waiting_the_page_refresh()
        self.pre_ask_for_leave_count = self.roll_call_page.get_ask_for_leave_count()
        assert self.pre_ask_for_leave_count == self.ask_for_leave_count + 1
        student_name_list = self.roll_call_page.get_all_name_under_the_tab()
        assert self.name in student_name_list
        
        
        # 进入学生的请假详情
        self.roll_call_page.go_to_student_leave_detail_page_by_name(name=self.name)
        deatil_page_student_name = self.student_leave_detail_page.get_student_name()
        # 学生姓名超过4个字会显示...
        name_tem = deatil_page_student_name[0:4]+'...' if len(deatil_page_student_name) > 3 else deatil_page_student_name
        detail_page_applicant = self.student_leave_detail_page.get_applicant_name()
        detail_page_days_count = self.student_leave_detail_page.get_day_count()
        detail_page_notes = self.student_leave_detail_page.get_notes()
        # assert self.name == name_tem
        teacher_name = self.client.config['teacher_config']['info']['name']
        assert teacher_name in detail_page_applicant
        assert detail_page_days_count == '0.5天'
        assert detail_page_notes == '6666'