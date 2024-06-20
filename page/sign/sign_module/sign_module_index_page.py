from base.teacher_client import TeacherClient
from common.appOperator import Operator
from elements.sign.sign_module.sign_module_index_page_elements import IndexPageElements
from page.sign.sign_index_page  import SignIndexPage
class SignModuleIndexPage:
    def __init__(self,client:TeacherClient,is_init_to_page:bool=True) -> None:
        self.client = client 
        self.operator = self.client.operator
        self.sign_index_page_elements = IndexPageElements()
        if is_init_to_page:
            SignIndexPage(self.client).goto_sign_module()
            
        
    def go_to_student_roll_call_page(self):
        self.operator.click(self.sign_index_page_elements.student_tab)
        self.operator.click(self.sign_index_page_elements.roll_call_btn)
        
    def go_to_teacher_roll_call_page(self):
        self.operator.click(self.sign_index_page_elements.teacher_tab)
        self.operator.click(self.sign_index_page_elements.roll_call_btn)
        
    
    def get_sign_person_name(self,index:int=0):
        '''
        获取签到列表的人员名称,默认取第一个
        '''
        elements = self.operator.find_elements(self.sign_index_page_elements.sign_name)
        name = elements[index].text
        return name