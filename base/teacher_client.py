from selenium import webdriver
from appium import webdriver
from common.appOperator import Operator
from page.login_page import LoginPage
from base.read_config import ReadConfig
# 初始化安装、重置、重启
desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '13'  # 设备系统版本
desired_caps['deviceName'] = 'c21fc2f5'  #  设备名称
desired_caps['appPackage'] = 'com.yuanding.seebaby'
desired_caps['appActivity'] = 'com.yuanding.seebaby.WelcomeActivity'
#相当于杀进程 
desired_caps['noReset'] = True
desired_caps['fullReset'] = False 


class  TeacherClient:
    __instance = None
    _is_inited = False
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance
    
    def __init__(self,is_need_restart=None,is_need_uninstall_app=False) :
        if  self._is_inited == False:
            self.config = ReadConfig().yml_datas
            self.device_config = self.config['device_config']
            # 初始化安装、重置、重启
            self.desired_caps = {}
            self.desired_caps['platformName'] = self.device_config['device']['platformName']  # 设备系统
            self.desired_caps['platformVersion'] = self.device_config['device']['platformVersion']  # 设备系统版本
            self.desired_caps['deviceName'] = self.device_config['device']['deviceName']  #  设备名称
            self.desired_caps['appPackage'] = self.device_config['app']['appPackage']
            self.desired_caps['appActivity'] = self.device_config['app']['appActiivty']
            self.desired_caps['newCommandTimeout'] = 120
            self.desired_caps['w3c'] = False
            self.desired_caps['automationName'] = 'UiAutomator2'
            # self.desired_caps['chromedriverExecutable'] = 'D:/104/chromedriver.exe'
            #相当于杀进程 
            self.desired_caps['noReset'] = self.device_config['app']['noReset']
            self.desired_caps['fullReset'] = self.device_config['app']['fullReset'] 
            
            
            # webdriver.Remote
            self.driver = webdriver.Remote(self.device_config['appium']['ip'],desired_caps)
            self.operator = Operator(self.driver)
            if desired_caps['fullReset'] or not desired_caps['noReset']:
                self._login()
            self._is_inited = True
            
        if is_need_restart:
            self.operator.start_activity(self.desired_caps['appPackage'],self.desired_caps['appActivity'])
            
        elif is_need_uninstall_app:
            self.operator.reset_app()
        
        
            
              
    
    def _login(self):
        login_page = LoginPage(self.driver)
        login_page.click_agree_btn()
        login_page.skip_intro_pic()
        login_page.login_by_account_success('11220221222','123456')