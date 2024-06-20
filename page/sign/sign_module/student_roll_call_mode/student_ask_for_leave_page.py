from elements.sign.sign_module.student_roll_call_page.ask_for_leave_for_student_elements import AskForLeaveForStudentElements
from base.teacher_client import TeacherClient
from page.sign.sign_module.sign_module_index_page import SignModuleIndexPage
# 学生请假页面
class StudentAskForLeavePage:
    def __init__(self,client:TeacherClient) -> None:
        self.client = client
        self.operator = self.client.operator
        self.student_ask_for_leave_elements = AskForLeaveForStudentElements()

    def select_leave_time(self,times:int=0):
        '''
        times:请假时长  
        0:上午
        1:下午
        2:今天
        3:多天
        
        '''
        if times == 0:
            self.operator.click(self.student_ask_for_leave_elements.time_tag_morning)
        elif times == 1:
            self.operator.click(self.student_ask_for_leave_elements.time_tag_aftertnoon)
        elif times == 2:
            self.operator.click(self.student_ask_for_leave_elements.time_tag_all_day)
        elif times == 3:
            self.operator.click(self.student_ask_for_leave_elements.time_tag_several_day) 
            
    def chose_reason_for_leave(self,leave_type:int=0):
        '''
        leave_type:请假原因 0：病假 1：事假
        '''
        if leave_type == 0:
            self.operator.click(self.student_ask_for_leave_elements.leave_tag_sick)
        elif leave_type == 1:
            self.operator.click(self.student_ask_for_leave_elements.leave_tag_business)                    
                
                
                
    def chose_sick_type(self,sick_type:int=0):
        '''
        病因：0：感冒 1：发烧 2：腹泻 3：水痘 4、手足口 5：腮腺炎 6：其他
        '''
        if sick_type == 0:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_cold)
        elif sick_type == 1:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_fever)
        elif sick_type == 2:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_diarrhea)
        elif sick_type == 3:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_chickenpox) 
        elif sick_type == 4:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_hfmd)
        elif sick_type == 5:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_mumps)
        elif sick_type == 6:
            self.operator.click(self.student_ask_for_leave_elements.sick_tag_others) 
            
    def fill_in_the_presentation_of_condition(self,text:str):
        self.operator.send_text(self.student_ask_for_leave_elements.apply_reason,text)
                        

    def _click_add_photh_btn(self):
        self.operator.click(self.student_ask_for_leave_elements.upload_btn)
        
    def _click_agree_btn(self):
        self.operator.click(self.student_ask_for_leave_elements.agree_btn)
        
    def _click_choose_photo_from_phone_btn(self):
        self.operator.click(self.student_ask_for_leave_elements.choose_photo_from_phone_btn)
        
    def _choose_one_pic(self,num:int=0):
        element = self.operator.find_elements(self.student_ask_for_leave_elements.choose_photo_btn)[num]
        self.operator.click(element)
        
    def _click_finish_btn(self):
        self.operator.click(self.student_ask_for_leave_elements.sys_album_finish_btn)
    
    
    def choose_picture(self):
        self._click_add_photh_btn()
        try :
            self._click_agree_btn()
        except :
            print('找不到同意按钮1')
        try :
            self.operator.agree_sys_alert()
        except:
            print('找不到同意按钮2')
        self._click_choose_photo_from_phone_btn()
        self._choose_one_pic()
        self._click_finish_btn()
            
    def submit_record(self):
        self.operator.click(self.student_ask_for_leave_elements.submit_btn)
        
    