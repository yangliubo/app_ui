import sys
BASE_DIR= 'e:\\python_project\\app_ui'
sys.path.append(BASE_DIR)
from page.sign.count_module.student_count_index_page import StudentCountIndexPage
from page.sign.temperature_module.student_temperature_detail_page import TemperatureDetailPage
from page.sign.temperature_module.student_temperature_count_page import StudentTemperatureCountPage
from elements.sign.count_module.student_count_index_page_element import StudentCountIndexPageElement
from base.teacher_client import TeacherClient
from appium.webdriver.common.mobileby import MobileBy
import pytest
import time
from assertpy import assert_that
@pytest.mark.ii
class TestSetTemperatureForStudent:
    def setup_class(self):
        self.client = TeacherClient()
        self.operator = self.client.operator
        self.student_count_index_page = StudentCountIndexPage(self.client)
        self.tem_count_page = StudentTemperatureCountPage(client = self.client,is_init_into_page=False)
        self.detail_page = TemperatureDetailPage(self.client)
        self.count_elements = StudentCountIndexPageElement()
        
    def test_set_temperature_for_student(self):        
        # 获取体温数据
        morning_normal_count = self.student_count_index_page.get_morning_normal_count()
        morning_fever_count = self.student_count_index_page.get_morning_fever_count()
        morning_notest_count = self.student_count_index_page.get_morning_notest_count()
        # 进入班级体温列表页
        self.student_count_index_page.goto_temperature_page()
        contexts = self.client.operator.get_contexts()
        current_context = self.client.operator.get_current_context()
        print('current:',current_context)
        print('all:',contexts)
        self.operator.switch_to_webview()
        cu = self.operator.get_current_context()
        print('切完了？：',cu)
        count = self.tem_count_page.get_row_count_info(1)
        print('未检测',count)
        # 进入班级体温详情页
        self.tem_count_page.go_to_class_temperature_detail_page_by_num()
        print('contexts有',self.operator.driver.contexts)
        cu = self.operator.get_current_context()
        print('当前页面context是',cu)
        self.operator.switch_to_navite()
        self.operator.switch_to_webview()
        all_window_handles = self.operator.driver.window_handles
        print('句柄都有哪些：',all_window_handles)
        current_handle = self.operator.driver.current_window_handle
        print('当前句柄是：',current_handle,self.operator.driver.current_url,self.operator.driver.title)
        self.operator.driver.switch_to.window(all_window_handles[-1])
        print('当前句柄是：',current_handle,self.operator.driver.current_url,self.operator.driver.title)
        self.detail_page.switch_tab(2)
        # 点击录入体温按钮
        self.detail_page.click_first_unchecked_student_fill_in_temperature_btn()
        # 提交一个正常体温的学生
        temperature = self.detail_page.get_temperature_untested()
        assert_that(temperature).is_equal_to('36.5')
        self.detail_page.add_temperature()
        self.detail_page.add_temperature()
        temperature = self.detail_page.get_temperature_untested()
        assert_that(temperature).is_equal_to('36.7')
        self.detail_page.subtract_temperautre()
        temperature_input_normal = self.detail_page.get_temperature_untested()
        assert_that(temperature_input_normal).is_equal_to('36.6')
        # 获取下要提交的学生姓名
        name = self.detail_page.get_first_student_name()
        # 提交
        self.detail_page.click_commit_btn()
        time.sleep(2)
        # 切换到正常列表
        self.detail_page.switch_tab(0)
        time.sleep(2)
        name_normal = self.detail_page.get_first_student_name()
        assert_that(name_normal).contains(name)
        temperature = self.detail_page.get_temperature_confirmed()
        assert_that(temperature).contains(temperature_input_normal)
        
        self.detail_page.switch_tab(2)
        # 提交一个发烧的学生
        self.detail_page.click_first_unchecked_student_fill_in_temperature_btn()
        self.detail_page.add_temperature_to_fever()
        temperature_input_fever = self.detail_page.get_temperature_untested()
        self.detail_page.click_commit_btn()
        name1 = self.detail_page.get_first_student_name()
        print('提交的发热姓名是',name1)
        # 切换到发热列表
        time.sleep(2)
        self.detail_page.switch_tab(1)
        time.sleep(2)
        name_fever = self.detail_page.get_first_student_name()
        assert_that(name_fever).contains(name1)
        temperature = self.detail_page.get_temperature_confirmed()
        assert_that(temperature).contains(temperature_input_fever)
        
        
        
        # 返回到班级统计列表页
        self.operator.switch_to_navite()
        self.detail_page.back_to_up_page()
        self.operator.switch_to_webview()
        cu = self.operator.get_current_context()
        print('当前页面context是',cu)
        self.operator.switch_to_window_by_url_contains('userType=1')
        print('当前句柄是：',current_handle,self.operator.driver.current_url,self.operator.driver.title)
        self.operator.web_refresh_page()
        count_1 = self.tem_count_page.get_row_count_info(1)
        print('返回后的数据：',count_1)
        assert_that(count_1['class_name']).is_equal_to(count['class_name'])
        assert_that(int(count_1['normal_count'])).is_equal_to(int(count['normal_count'])+1)
        assert_that(int(count_1['fever_count'])).is_equal_to(int(count['fever_count'])+1)
        assert_that(int(count_1['no_test_count'])).is_equal_to(int(count['no_test_count'])-2)
        self.operator.switch_to_navite()
        # 返回到统计首页
        self.tem_count_page.back_to_up_page()
        # 刷新页面
        self.operator.swip_to_bottom_half_in_window()
        # 获取体温数据
        morning_normal_count1 = self.student_count_index_page.get_morning_normal_count()
        morning_fever_count1 = self.student_count_index_page.get_morning_fever_count()
        morning_notest_count1 = self.student_count_index_page.get_morning_notest_count()
        assert_that(int(morning_normal_count1)).is_equal_to(int(morning_normal_count)+1)
        assert_that(int(morning_fever_count1)).is_equal_to(int(morning_fever_count)+1)
        assert_that(int(morning_notest_count1)).is_equal_to(int(morning_notest_count)-2)