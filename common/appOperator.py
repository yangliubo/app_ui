from appium.webdriver.webdriver import WebDriver 
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from common.element_info import ElementInfo
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.actions.pointer_actions import PointerActions
class Operator:
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
    
    def web_refresh_page(self):
        self.driver.refresh()
        
    def get_contexts(self):
        return self.driver.contexts
        
    def get_current_context(self):
        return self.driver.context
    
    def get_windows_handles(self):
        return self.driver.window_handles
    
    def get_current_handle(self):
        return self.driver.current_window_handle
    
    def switch_to_window_by_url_contains(self,url_contains:str):
        handles = self.get_windows_handles()
        for i in handles:
            self.driver.switch_to_window(i)
            if url_contains in self.driver.current_url:
                return
            
    def switch_to_webview(self):
        contexts = self.get_contexts()
        for i in contexts:
            if 'WEBVIEW' in i :
                self.driver.switch_to.context(i)
                break
                
    def switch_to_navite(self):
        contexts = self.get_contexts()
        for i in contexts:
            if 'NATIVE' in i :
                self.driver.switch_to.context(i)
                break
    
    def click(self,element):
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        webelement.click()
    
    def send_text(self,element,text):
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        webelement.set_text(text)
    
    def start_activity(self,package_name,activity_name):
        self.driver.start_activity(package_name,activity_name)
        
    def reset_app(self):
        self.driver.reset()
        
    def get_window_size(self):
        size = self.driver.get_window_size()
        # print('.........................',size)
        # 返回格式  {'width': 1440, 'height': 3063}
        return size
    
    def get_element_attribute_by_name(self,element,attribute_name):
        '''根据元素、属性名获取某个元素的属性'''
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        return webelement.get_attribute(name=attribute_name)
        
        
    def get_location(self,element):
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        location1 = webelement.location
        return location1
    
    
    def get_rect(self,element):
        '''
        获取元素宽高以及左上角的坐标  {'height': 158, 'width': 402, 'x': 755, 'y': 2363}
        '''
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        print('列表区域：',webelement)
        webelement._w3c=True
        print('eeeeeeeeeeeeeeeeeeeee w3c开关:',webelement._w3c)
        rect = webelement.rect
        return rect
    
    def get_text(self,element):
        '''获取元素的文案'''
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        text = webelement.text
        return text
    
    def scrolled_element_into_view(self,element):
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        webelement.location_once_scrolled_into_view()    
        
    # 多种滑动方式
    def swip(self,start_x, start_y, end_x, end_y, duration=None):
        self.driver.swipe(start_x=start_x,start_y=start_y,end_x=end_x,end_y=end_y,duration=duration)
    
    def swip_top_half_in_element_zone(self,element):
        '''在指定的元素区域内内向上滑动一半'''
        # 获取元素左上角坐标
        rect = self.get_rect(element)
        x = rect['x']
        y = rect['y']
        height = rect['height']
        width = rect['width']
        start_x = end_x = (x+width)//2
        start_y = (y+height)*3//4
        end_y = (y+height)//4
        self.swip(start_x=start_x,start_y=start_y,end_x=end_x,end_y=end_y)
        
    def swip_to_bottom_half_in_element_zone(self,element):
        '''在指定的元素区域内内向下滑动一半,可用于原生下拉刷新'''
        # 获取元素左上角坐标
        rect = self.get_rect(element)
        x = rect['x']
        y = rect['y']
        height = rect['height']
        width = rect['width']
        start_x = end_x = (x+width)//2
        end_y = (y+height)*3//4
        start_y = (y+height)//4
        print('开始刷新')
        print('开始坐标：',(start_x,start_y),'结束坐标：',(end_x,end_y))
        self.swip(start_x=start_x,start_y=start_y,end_x=end_x,end_y=end_y,duration=2000)
        print('结束刷新')
        
    def swip_to_bottom_half_in_window(self):
        size = self.get_window_size()
        height = size['height']
        width = size['width']
        start_x = width//2
        start_y = height//2
        end_x = start_x
        end_y = height*3//4
        self.swip(start_x=start_x,start_y=start_y,end_x=end_x,end_y=end_y,duration=2000)
        
        
        
    def swipe_left(self,duration:int=200):
        '''快速左滑'''
        size = self.get_window_size()
        x = size['width']
        y = size['height']
        half_x = x//2
        half_y = y//2
        end_x = half_x//2
        self.driver.swipe(start_x=half_x,start_y=half_y,end_x=end_x,end_y=half_y,duration=duration)
    
    def flick_left(self):
        size = self.get_window_size()
        x = size['width']
        y = size['height']
        half_x = x//2
        half_y = y//2
        end_x = half_x//2
        self.driver.flick(start_x=half_x,start_y=half_y,end_x=end_x,end_y=half_y)
        
    def web_drag_and_drop_by_offset(self,element,x,y):
        '''
        拖拽元素到指定坐标 x,y
        '''
        actions = ActionChains(self.driver)
        webelement = element if isinstance(element,WebElement) else self.find_element(element)
        actions.drag_and_drop_by_offset(webelement, x, y).perform() 
        
    def web_swip_to_bottom_half_in_element_zone(self,element):
        # 获取元素左上角坐标
        rect = self.get_rect(element)
        x = rect['x']
        y = rect['y']
        height = rect['height']
        end_x = 0
        end_y = (y+height)//2
        self.web_drag_and_drop_by_offset(element=element,x=end_x,y=end_y)
        
    def web_scroll_from_element(self,element,xoffset,yoffset):
        # web_element = element if isinstance(element,WebElement) else self.find_element(element=element)
        # action = TouchActions(self.driver)
        # action.scroll_from_element(web_element,xoffset,yoffset)
        # action.perform()
        point_action = PointerActions()
        point_action.click_and_hold(element)
        point_action.move_to_location()
        
    def web_excute_script(self,script):
        self.driver.execute_script(script)
        
        
    def determine_elements_is_overlap(self,element_1,element_2):
        '''
        判断两个元素是否有重叠
        '''
        el1 = element_1 if isinstance(element_1,WebElement) else self.find_element(element_1)
        el2 = element_2 if isinstance(element_2,WebElement) else self.find_element(element_2)
        el1_rect = self.get_rect(el1)
        el2_rect = self.get_rect(el2)
        # 获取2个元素的起止点坐标
        e1_x1 = el1_rect['x']
        e1_x2 = e1_x1+el1_rect['width']
        e2_x1 = el2_rect['x']
        e2_x2 = e2_x1 + el2_rect['width']
        e1_y1 = el1_rect['y']
        e1_y2 = e1_y1 + el1_rect['height']
        e2_y1 = el2_rect['y']
        e2_y2 = e2_y1 + el2_rect['height']
        # 判断4个点都不在对方元素的对应的x轴y轴区间内即为不重叠，x轴没有交叉 或y轴没有交叉
        if ((e1_x1 > e2_x2 ) and ( e1_x2 > e2_x1)) or ((e1_y1 > e2_y2) and (e1_y2 < e2_y1)) :
            
            return True
        else:
            return False
        
    def determine_element_is_overlaped_with_zone(self,element,zone_rect:tuple=()):
        '''
        判断元素和区域是否有重叠
        zone_rect：区域的元组，包含起止的坐标eg： ((x1,y1),(x2,y2))
        '''
        el1 = element if isinstance(element,WebElement) else self.find_element(element)
        el1_rect = self.get_rect(el1)
        # 获取2个元素的起止点坐标
        e1_x1 = el1_rect['x']
        e1_x2 = e1_x1+el1_rect['width']
        e2_x1 = zone_rect[0][0]
        e2_x2 = zone_rect[1][0]
        e1_y1 = el1_rect['y']
        e1_y2 = e1_y1+el1_rect['height']
        e2_y1 = zone_rect[0][1]
        e2_y2 = zone_rect[1][1]
        # 判断x轴没有交叉 或y轴没有交叉 即为不重叠
        if ((e1_x1 > e2_x2 ) or ( e1_x2 < e2_x1)) or ((e1_y1 > e2_y2) or (e1_y2 < e2_y1)) :
            return False
        else:
            return True
        
        
    def determine_element_is_checked(self,element):
        '''判断元素是否被选中'''
        el1 = element if isinstance(element,WebElement) else self.find_element(element)
        is_checked = el1.get_attribute(name='checked')
        if is_checked :
            return True
        else :
            return False
        
    
    # 滑动直到找到某个元素
    # 1、先找到区域坐标 2、从x*3/4滑动到x*1/4处 3、查找元素 （如果元素的位置没有变化就不再滑动）2、滑动元素到区域中间
        
    def find_element(self,element:ElementInfo):

        if element.expect_condition == 'element_to_be_clickable':
            web_element = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(EC.element_to_be_clickable((element.locator_type,element.locator_value)))
        elif element.expect_condition == 'text_in_elements':
            web_elements = self.find_elements(element)
            for i in web_elements :
                if i.text == element.expect_value:
                    web_element = i
        elif element.locator_type == 'id':
            web_element = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_element_by_id(element.locator_value))
        elif element.locator_type == '-android uiautomator':
            web_element = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_element_by_android_uiautomator(element.locator_value))
        elif element.locator_type == MobileBy.CSS_SELECTOR:
            web_element = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_element_by_css_selector(element.locator_value))
        elif element.locator_type == MobileBy.XPATH:
            web_element = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_element_by_xpath(element.locator_value))

        return web_element
    
    
    def find_elements(self,element:ElementInfo):

        if element.expect_condition == 'element_to_be_clickable':
            web_elements = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(EC.element_to_be_clickable())

        if element.locator_type == MobileBy.ID:
            web_elements = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_elements_by_id(element.locator_value))
        if element.locator_type == MobileBy.CSS_SELECTOR:
            web_elements = WebDriverWait(self.driver,timeout=element.timeout,poll_frequency=element.poll_frequency).until(lambda x:x.find_elements_by_css_selector(element.locator_value))

        return web_elements
    
    def find_child_element(self,father_element,element:ElementInfo):
        fa_element = father_element if isinstance(father_element,WebElement) else self.find_element(father_element)
        if element.locator_type == MobileBy.ID:
            element = fa_element.find_element_by_id(element.locator_value)
        if element.locator_type == MobileBy.CSS_SELECTOR:
            element = fa_element.find_element_by_css_selector(element.locator_value)
        return element
    
    def get_page_source(self):
        page_source = self.driver.page_source
        return page_source
    
    
    # Android系统弹窗
    def agree_sys_alert(self):
        # self.driver.click(self.driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")'))
        ele = WebDriverWait(self.driver,timeout=3,poll_frequency=0.5).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("始终允许")'))
        ele.click()
    # self.appOperator.reset_app()

        
    # self.appOperator.start_activity('com.yuanding.seebaby','com.yuanding.seebaby.WelcomeActivity')
        