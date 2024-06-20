from base.teacher_client import TeacherClient
from elements.sign.temperature.student_temperature_detail_elements import StudentTemperatureDetailElements
import time

class TemperatureDetailPage:
    def __init__(self,client:TeacherClient) -> None:
        self.client = client
        self.operator = self.client.operator
        self.detail_elements = StudentTemperatureDetailElements()
        
    def switch_tab(self,type:int=0):
        '''
        TYPE:TAB类型 0正常 1发热 2未检测
        '''
        if type == 0:
            self.operator.click(self.detail_elements.tab_normal)
        elif type == 1:
            self.operator.click(self.detail_elements.tab_fever)
        elif type == 2:
            self.operator.click(self.detail_elements.tab_untested)
    
    def click_first_unchecked_student_fill_in_temperature_btn(self):
        '''
        点击第一个学生录入体温按钮
        '''
        first_fill_in_eles = self.operator.find_elements(self.detail_elements.fill_in_temperature_btns)
        self.operator.click(first_fill_in_eles[0])
        
    def click_cancel_btn(self):
        '''
        点击取消按钮
        '''
        self.operator.click(self.detail_elements.cancel_btn)
        
    def click_commit_btn(self):
        '''
        点击提交按钮
        '''
        self.operator.click(self.detail_elements.commit_btn)
        
    def add_temperature(self):
        '''
        点击增加体温
        '''
        self.operator.click(self.detail_elements.add_btn)
        
    def subtract_temperautre(self):
        '''
        点击减少体温
        '''
        self.operator.click(self.detail_elements.subtract_btn)
        
    def get_status_untested(self):
        '''
        获取体温状态
        '''
        text = self.operator.get_text(self.detail_elements.status)
        return text
    
    def get_temperature_untested(self):
        '''
        获取输入的体温
        '''
        text = self.operator.get_element_attribute_by_name(self.detail_elements.temperature_input,attribute_name='aria-valuenow')
        print('tttttttttttttttttttttttt',text)
        return text
    
    def add_temperature_to_fever(self):
        for i in range(10):
            # time.sleep(1)
            self.add_temperature()

    def get_first_student_name(self):
        eles = self.operator.find_elements(self.detail_elements.names)
        first_ele = eles[0]
        name = self.operator.get_text(first_ele)
        return name
     
    def get_temperature_confirmed(self,num:int=0):
        '''获取正常和发热列表的学生体温 num 默认0列表第一个'''
        eles = self.operator.find_elements(self.detail_elements.temperature)
        ele = eles[num]
        text = self.operator.get_text(ele)
        return text
    
    def back_to_up_page(self):
        '''点击返回上一页'''
        self.operator.click(self.detail_elements.back_btn)
        