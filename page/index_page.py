from base.teacher_client import TeacherClient
from elements.index_page_elements import IndexPageElements
import time
class IndexPage:
    def __init__(self,client:TeacherClient) -> None:
        self.client = client 
        self.operator = self.client.operator
        self.index_page_elements = IndexPageElements()
    
    def _determine_element_is_hide_by_other_element(self,element_to_be_determined,element):
        '''在这个页面，判断y轴就可以了'''
        webelement_d_rect = self.operator.get_rect(element_to_be_determined)
        webelement_rect = self.operator.get_rect(element)
        webelement_d_y_end = webelement_d_rect['y']+webelement_d_rect['height']
        webelement_y =webelement_rect['y']
        if webelement_d_y_end > webelement_y:
            return True
        else:
            return False
    
    def swip_until_find_module(self,module_name):
        while True:
            previous_modules = self.operator.find_elements(self.index_page_elements.modules)
            for module in previous_modules:
                if module.text == module_name and not self._determine_element_is_hide_by_other_element(module,self.index_page_elements.publish_btn):
                    return
            previous_last_name = previous_modules[-1].text
            self.operator.swip_top_half_in_element_zone(element=self.index_page_elements.modules_swip_zone)
            time.sleep(2)
            modules = self.operator.find_elements(self.index_page_elements.modules)
            last_name = modules[-1].text
            if previous_last_name == last_name:
                return
            
    def goto_sign(self):
        self.swip_until_find_module(module_name='签到')
        self.operator.click(self.index_page_elements.sign_module)

    