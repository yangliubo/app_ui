import sys
BASE_DIR= 'e:\\python_project\\app_ui'
sys.path.append(BASE_DIR)

from page.sign.temperature_module.student_temperature_detail_page import TemperatureDetailPage
from page.sign.temperature_module.student_temperature_count_page import StudentTemperatureCountPage
from elements.sign.temperature.student_count_page_by_class_elements import StudentTemperatureCountPageElements
from base.teacher_client import TeacherClient
from appium.webdriver.common.mobileby import MobileBy
import pytest
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop

@pytest.mark.r
class TestSetTemperatureForStudent:
    def setup_class(self):
        self.client = TeacherClient()
        self.operator = self.client.operator
        # self.student_count_index_page = StudentCountIndexPage(self.client)
        self.tem_count_page = StudentTemperatureCountPage(self.client)
        self.detail_page = TemperatureDetailPage(self.client)
        self.e = StudentTemperatureCountPageElements()
        
    def test_set_temperature_for_student(self):
        # self.student_count_index_page.goto_temperature_page()
        # self.operator.swip_to_bottom_half_in_element_zone(self.e.list_zone_native)
        contexts = self.client.operator.get_contexts()
        current_context = self.client.operator.get_current_context()
        print('current:',current_context)
        print('all:',contexts)
        self.operator.switch_to_webview()
        cu = self.operator.get_current_context()
        print('切完了？：',cu)
        count = self.tem_count_page.get_row_count_info(1)
        print('未检测',count)
        self.operator.switch_to_window_by_url_contains('userType=1')
        print('当前句柄是：',self.operator.driver.current_url,self.operator.driver.title)
        ea = self.operator.find_element(self.e.list_zone)
        el = self.tem_count_page.get_row_ele_by_num()
        el2 = self.tem_count_page.get_row_ele_by_num(5)
        # self.operator.web_drag_and_drop_by_offset(ea,x=0,y=300)
        
        # self.operator.swip_to_bottom_half_in_element_zone(el)
        # self.operator.driver.swipe(start_x=469,start_y=277,end_x=469,end_y=1547,duration=2000)
        # self.operator.web_scroll_from_element(self.e.list_zone,0,100)
        
        # 行不通不是标准的w3c协议
        # action = TouchActions(self.operator.driver)
        # action.long_press(el)
        # action.move(469,1547)
        # action.perform()
        # action.release(469,1547)
        # slide_script = 'arguments[0].scrollTop += 300;'
        # self.operator.driver.execute_script(slide_script,el)
        # self.operator.driver.execute_script(slide_script,el)
        # self.operator.driver.execute_script(slide_script,el)
        # self.operator.driver.execute_script(slide_script,el)
        
        # action = ActionChains(self.operator.driver)
        # action.click_and_hold(el)
        # print('点到了？？？')
        # action.move_to_element(el2)
        # print('移动到了？？？？')
        # time.sleep(3)
        # action.release()
        # # action.drag_and_drop(el,el2)
        # action.perform()
        
        # for i in range(10):
        #     drag_and_drop(self.operator.driver, el, el2)
        #     time.sleep(2)
        

        # action = ActionChains(self.operator.driver)
        # for i in range(10):
        #     ActionChains(self.operator.driver).click_and_hold(ea).perform()       
        #     ActionChains(self.operator.driver).move_by_offset(0, 100).perform()
        #     ActionChains(self.operator.driver).move_by_offset(0, 100).perform()
        #     print('点到了？？？')
        #     ActionChains(self.operator.driver).release().perform()
        
        print('找到元素了 开始刷新页面')
        # self.operator.driver.refresh()
        time.sleep(5)
        self.operator.driver.execute_script('location.reload();')