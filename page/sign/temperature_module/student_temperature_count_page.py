from base.teacher_client import TeacherClient
from elements.sign.temperature.student_count_page_by_class_elements import StudentTemperatureCountPageElements
from page.sign.count_module.student_count_index_page import StudentCountIndexPage
import time

class StudentTemperatureCountPage:
    def __init__(self,client:TeacherClient,is_init_into_page:bool=True) -> None:
        self.client = client
        self.operator = self.client.operator
        self.count_page_elements = StudentTemperatureCountPageElements()
        if is_init_into_page == True:
            StudentCountIndexPage(client=self.client).goto_temperature_page()
     
    def get_row_ele_by_num(self,num:int=1):
        # 循环10s  因为标题栏和列表的元素class是一样的,可能出现列表元素没有加载出来
        for i in range(10):
            rows = self.operator.find_elements(self.count_page_elements.rows)
            if len(rows) >1:
                row_ele = rows[num]
                return row_ele  
            else :
                time.sleep(1)
           
      
    def go_to_class_temperature_detail_page_by_num(self,num:int=1):
        '''
        点击进入体温详情页
        num: 行数 第一行即为1 （第0行为标题）
        '''
        row_ele = self.get_row_ele_by_num(num)
        self.operator.click(row_ele)
        
    def get_row_count_info(self,row_num:int=0):
        '''
        获取列表某一行的信息：班级名称、正常、发烧、未检测
        num: 行数 第一行即为1 （第0行为标题）
        '''
        el = self.get_row_ele_by_num(row_num)
        class_name = self.operator.find_child_element(father_element=el,element=self.count_page_elements.class_name)
        normal_count = self.operator.find_child_element(father_element=el,element=self.count_page_elements.normal_count)
        fever_count = self.operator.find_child_element(father_element=el,element=self.count_page_elements.hot_count)
        count_ele = self.operator.find_child_element(father_element=el,element=self.count_page_elements.not_test_count)
        return {'class_name':class_name.text,'normal_count':normal_count.text,'fever_count':fever_count.text,'no_test_count':count_ele.text}
    
    def back_to_up_page(self):
        self.operator.click(self.count_page_elements.back_btn)
        