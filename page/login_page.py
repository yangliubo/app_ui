from common.appOperator import Operator
from elements.login_page import LoginPageElements
import time
class LoginPage():
    def __init__(self,driver):
        self.operator = Operator(driver)
        self.loginPage_element = LoginPageElements()
    
    def click_agree_btn(self):
        self.operator.get_rect(self.loginPage_element.privacy_agreement_btn)
        self.operator.click(self.loginPage_element.privacy_agreement_btn)
        
    def _find_buttom_sliding_btn(self):
        element = self.operator.find_element(self.loginPage_element.buttom_sliding_btn)
        return element
    
    def _find_experience_btn(self):
        element = self.operator.find_element(self.loginPage_element.experience_btn)
        return element
    
    def _click_experience_btn(self):
        self.operator.click(self.loginPage_element.experience_btn)     
        
    def skip_intro_pic(self):
        self._find_buttom_sliding_btn()
        i = 0
        while i < 10:
            self.operator.swipe_left()
            i += 1
            if i > 3 and self._find_experience_btn() is not None:
                break
            time.sleep(1)
        self._click_experience_btn()
    
    def click_login_by_account_btn(self):
        self.operator.click(self.loginPage_element.login_by_account_btn)
        
    def input_account(self,account_text):
        self.operator.send_text(element=self.loginPage_element.account_input,text=account_text)
    
    def input_passwd(self,passwd_text):
        self.operator.send_text(element=self.loginPage_element.passwd_input,text=passwd_text)
    
    def click_login_btn(self):
        self.operator.click(self.loginPage_element.login_btn)
        
    def agree_deal(self):
        self.operator.click(self.loginPage_element.agree_deal_btn)
    
    def login_by_account_success(self,account_text,passwd_text):
        self.click_login_by_account_btn()
        self.input_account(account_text)
        self.input_passwd(passwd_text)
        self.agree_deal()
        self.click_login_btn()
        