from elements.sign.sign_module.student_roll_call_page.ask_for_leave_for_student_elements import AskForLeaveForStudentElements
from base.teacher_client import TeacherClient
from page.sign.sign_module.sign_module_index_page import SignModuleIndexPage
from elements.sign.sign_module.student_roll_call_page.student_ask_for_leave_detail_page_elements import StudentAskForLeaveDetailPageElements
# 学生请假详情页面
class StudentAskForLeaveDetailPage:
    def __init__(self,client:TeacherClient) -> None:
        self.client = client
        self.operator = self.client.operator
        self.detail_elements = StudentAskForLeaveDetailPageElements()
        
    def get_student_name(self):
        text = self.operator.get_text(self.detail_elements.student_name)
        return text
        
    def get_applicant_name(self):
        text = self.operator.get_text(self.detail_elements.applicant_info)
        return text
        
    def get_day_count(self):
        text = self.operator.get_text(self.detail_elements.leave_days)
        return text
        
    def get_start_time(self):
        text = self.operator.get_text(self.detail_elements.start_time)
        return text
    
    def get_end_time(self):
        text = self.operator.get_text(self.detail_elements.end_time)
        return text
    
    def get_reason(self):
        text = self.operator.get_text(self.detail_elements.reason)
        return text
    
    def get_status(self):
        text = self.operator.get_text(self.detail_elements.status)
        return text

    def get_notes(self):
        notes = self.operator.get_text(self.detail_elements.notes)
        return notes