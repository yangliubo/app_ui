from elements.sign.count_module.student_count_index_page_element import StudentCountIndexPageElement
from base.teacher_client import TeacherClient
from page.sign.sign_index_page import SignIndexPage

class StudentCountIndexPage:
    def __init__(self,client:TeacherClient,is_init_into_page:bool=True):
        self.client = client
        self.student_count_index_page_element = StudentCountIndexPageElement()
        self.operator = self.client.operator
        if is_init_into_page:
            SignIndexPage(self.client)
            
    def goto_temperature_page(self):
        self.operator.click(self.student_count_index_page_element.temperature_count_card)
    
    def get_morning_normal_count(self):
        morning_normal_el = self.operator.find_elements(self.student_count_index_page_element.temperature_count_normal_counts)[0]
        count = self.operator.get_text(morning_normal_el)
        return count

    def get_morning_fever_count(self):
        el = self.operator.find_elements(self.student_count_index_page_element.temperature_count_fever_counts)[0]
        count = self.operator.get_text(el)
        return count

    def get_morning_notest_count(self):
        el = self.operator.find_elements(self.student_count_index_page_element.temperature_count_notest_counts)[0]
        count = self.operator.get_text(el)
        return count