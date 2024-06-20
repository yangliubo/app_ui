from elements.sign.sign_module.student_roll_call_page.student_roll_call_page_elements import StudentRollCallElements
from base.teacher_client import TeacherClient
from page.sign.sign_module.sign_module_index_page import SignModuleIndexPage
import time
class StudentRollCallPage:
    def __init__(self,client:TeacherClient,is_init_to_page:bool=True) -> None:
        self.client = client
        self.operator = self.client.operator
        self.student_roll_call_elements = StudentRollCallElements()
        if is_init_to_page :
            SignModuleIndexPage(self.client).go_to_student_roll_call_page()
            
    def skip_guide_page(self):
        # 检测是否有引导页面
        try:
            page = self.operator.find_element(self.student_roll_call_elements.guide_page)
            if page:
                i = 0 
                while True:
                    self.operator.click(self.student_roll_call_elements.guide_know_more_btn)
                    if i == 4:
                        break
                    i += 1
        except:
            print('没有找到引导页面')
                
    def choose_class(self):
        self.operator.click(self.student_roll_call_elements.classes_btn)
        
    # def get_name_and_sign_status(self):
    #     student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
    #     student_info_list = []
    #     for i in student_list:
    #         student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
    #         sign_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_sign_status)
    #         print(student_name_el.text,sign_status.text)
    #         student_info_list.append({'element':i,'name':student_name_el.text,'status':sign_status.text})
    #     return student_info_list
            
    def find_first_unsigned_student(self):
        '''
        获取第一个没有签到的学生
        '''
        while True:
            student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
            last_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
            last_student_name = last_student_name_el.text
            print('last_student_name:',last_student_name)
            for i in student_list:
                sign_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_sign_status)
                leave_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_leave_status)
                student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                if sign_status.text == '签到' and leave_status.text == '请假':
                    student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                    return {'sign_status_element':sign_status,'name':student_name_el.text}
            else :
                self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
                student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
                pervious_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
                pervious_student_name = pervious_student_name_el.text
                if pervious_student_name == last_student_name:
                    print('到底了还没找到可以签到的学生')
                    return 

    def find_first_no_sign_out_student(self):
        '''
        获取第一个没有签退的学生
        '''
        while True:
            student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
            last_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
            last_student_name = last_student_name_el.text
            print('last_student_name:',last_student_name)
            for i in student_list:
                sign_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_sign_status)
                student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                if sign_status.text == '签退' :
                    student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                    return {'sign_status_element':sign_status,'name':student_name_el.text}
            else :
                self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
                student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
                pervious_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
                pervious_student_name = pervious_student_name_el.text
                if pervious_student_name == last_student_name:
                    print('到底了还没找到可以签退的学生')
                    return 
                
    def find_first_no_leave_student(self):
        '''
        获取第一个没有请假的学生,并返回 姓名、请假状态元素
        '''
        student_list = None
        while True:
            if student_list == None:
                student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
            # 找最后一个学生
                last_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
                last_student_name = last_student_name_el.text
            print('last_student_name:',last_student_name)
            for i in student_list:
                try:
                    leave_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_leave_status)
                    student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                    if leave_status.text == '请假' :
                        student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                        return {'leave_status_element':leave_status,'name':student_name_el.text}
                except:
                    continue
            self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
            
            student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
            
            print('滑动后的student_list',student_list)
            # 滑动后找到当前页面学生列表最后一个元素
            try:
                pervious_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
                pervious_student_name = pervious_student_name_el.text
            except:
                pervious_student_name_el = self.operator.find_child_element(father_element=student_list[-2],element=self.student_roll_call_elements.student_name)
                pervious_student_name = pervious_student_name_el.text
            print('pervious_student_name:',pervious_student_name)
            if pervious_student_name == last_student_name:
                print('到底了还没找到可以请假的学生')
                return 
            last_student_name = pervious_student_name
            
            
    def get_find_first_no_leave_student(self,last_student_name:str=None):
        print('之前最后的学生姓名是：',last_student_name)
        student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
        # 找列表最后一个学生,通过父元素找子元素有可能找不到（find_child_element）
        try:
            last_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
            current_last_student_name = last_student_name_el.text
        except :
            last_student_name_el = self.operator.find_child_element(father_element=student_list[-2],element=self.student_roll_call_elements.student_name)
            current_last_student_name = last_student_name_el.text
        print('current_last_student_name:',current_last_student_name)
        if current_last_student_name == last_student_name:
            print('没找到啊啊啊啊啊')
            return 
        
        for i in student_list:
            try:
                leave_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_leave_status)
                if leave_status.text == '请假' :
                    print('进来了')
                    student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                    print('找到的元素是',student_name_el.text,leave_status)
                    return {'leave_status_element':leave_status,'name':student_name_el.text}
            except:
                # 列表第一个元素  有可能被遮挡，通过父元素找子元素找不到  因此可以直接跳过
                continue

        self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
        return self.get_find_first_no_leave_student(last_student_name=current_last_student_name)
        
    def get_student_status_by_name():
        pass
            
    def sign_first_unsigned_student(self):
        '''
        给列表第一个没有签到的学生点名签到
        '''
        student_info = self.find_first_unsigned_student()
        self.operator.click(student_info['sign_status_element'])
        return student_info['name']
    
    def sign_first_no_sign_out_student(self):
        '''
        给列表第一个没有签退的学生点名签退
        '''
        student_info = self.find_first_no_sign_out_student()
        self.operator.click(student_info['sign_status_element'])
        return student_info['name']
    
    def ask_for_leave_for_first_student(self):
        '''
        给第一个没有请假的学生请假
        '''
        # student_info = self.find_first_no_leave_student()
        student_info = self.get_find_first_no_leave_student()
        print('找到了学生信息：',student_info)
        self.operator.click(student_info['leave_status_element'])
        return {'leave_status_element':student_info['leave_status_element'],'name':student_info['name']}
    
    def get_tab_elements(self):
        '''
        获取3个tab的元素
        '''
        tabs = self.operator.find_elements(self.student_roll_call_elements.tab)
        for tab in tabs:
            
            if '未签' in tab.text:
                unsigned_tab = tab
            elif '已签' in tab.text:
                signed_tab = tab
            else :
                all_tab = tab
        return{'all_tab':all_tab,'unsigned_tab':unsigned_tab,'signed_tab':signed_tab}
    
    def get_sign_and_unsigned_students_num(self):
        '''
        获取签到和未签到的个数
        '''
        tab_elements = self.get_tab_elements()
        unsigned_count = tab_elements['unsigned_tab'].text.split('(')[1].split(')')[0]
        sign_count = tab_elements['signed_tab'].text.split('(')[1].split(')')[0]
        return {'sign_count':int(sign_count),'unsigned_count':int(unsigned_count)}
    
    def switch_to_signed_tab(self):
        '''
        切换到已签tab--已签到
        '''
        tab_elements = self.get_tab_elements()
        self.operator.click(tab_elements['signed_tab'])
        
    def switch_to_unsigned_tab(self):
        tab_elements = self.get_tab_elements()
        self.operator.click(tab_elements['unsigned_tab'])

    def switch_to_all_tab(self):
        tab_elements = self.get_tab_elements()
        self.operator.click(tab_elements['all_tab'])    
        
    def get_all_name_under_the_tab(self):
        '''
        获取tab下所有的人名，可能超过一页需要滑动判断
        '''
        student_list = self.operator.find_elements(self.student_roll_call_elements.student_name)
        student_name_list = [i.text for i  in student_list]  
        student_set = set()
        student_set.update(student_name_list)
        while True:
            self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
            student_list = self.operator.find_elements(self.student_roll_call_elements.student_name)
            current_student_name_list = [i.text for i  in student_list]  
            if student_name_list == current_student_name_list:
                break
            else:
                student_set.update(current_student_name_list)
                student_name_list = current_student_name_list
        print(student_set)
        return student_set

    def back_to_superior_page(self):
        self.operator.click(self.student_roll_call_elements.back_btn)
        
    def switch_sign_mode(self):
        '''
        切换签到签退
        '''
        self.operator.click(self.student_roll_call_elements.sign_switch_btn)
        
    def get_ask_for_leave_count(self):
        leave_info = self.operator.get_text(self.student_roll_call_elements.tip_ask_for_leave_info)
        print('请假信息',leave_info)
        count = leave_info.split('假')[1].split('人')[0]
        return int(count)
    
    def click_tips_leave_info(self):
        self.operator.click(self.student_roll_call_elements.tip_ask_for_leave_info)
        
    def _get_student_status_ele_by_name(self,name):
        # 遍历查找学生
        while(True):
            student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
            last_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
            last_student_name = last_student_name_el.text
            print('last_student_name:',last_student_name)
            for i in student_list:
                
                student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                print('请假的学生姓名：',student_name_el.text)
                if student_name_el.text == name:
                    leave_status = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_leave_status)
                    student_name_el = self.operator.find_child_element(father_element=i,element=self.student_roll_call_elements.student_name)
                    return leave_status
            else :
                self.operator.swip_top_half_in_element_zone(element=self.student_roll_call_elements.list_zone)
                student_list = self.operator.find_elements(self.student_roll_call_elements.student_row)
                # 获取滑动后最后一个学生的姓名
                pervious_student_name_el = self.operator.find_child_element(father_element=student_list[-1],element=self.student_roll_call_elements.student_name)
                pervious_student_name = pervious_student_name_el.text
                if pervious_student_name == last_student_name:
                    print('到底了还没找到对应的学生')
                    return 
        

    def get_student_status_text_by_name(self,name):
        ele = self._get_student_status_ele_by_name(name)
        text = self.operator.get_text(ele)
        return text
    
    def go_to_student_leave_detail_page_by_name(self,name:str):
        '''
        进入某个学生的请假详情
        name:请假学生姓名
        '''
        ele = self._get_student_status_ele_by_name(name)
        self.operator.click(ele) 
        
    def waiting_the_page_refresh(self):
        # 等待页面刷新完成
        while (True):
            ele = self.operator.find_element(self.student_roll_call_elements.refresh_btn)
            print(ele.text)
            if ele.text == '下拉可以刷新':
                return
            time.sleep(1)