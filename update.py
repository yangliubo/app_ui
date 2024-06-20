# from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '13'  # 设备系统版本
desired_caps['deviceName'] = 'c21fc2f5'  #  设备名称
desired_caps['appPackage'] = 'com.yuanding.seebaby'
desired_caps['appActivity'] = 'com.yuanding.seebaby.WelcomeActivity'
#相当于杀进程 
desired_caps['noReset'] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# desired_caps['fullReset'] = False

time.sleep(5)
print('sleep完了')
# 立即升级按钮com.yuanding.seebaby:id/btn_update
WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_id("com.yuanding.seebaby:id/btn_update")).click()
# driver.find_element_by_id('com.yuanding.seebaby:id/btn_update').click()
print('??????????????????')
# 应用商店 com.huawei.appmarket:id/hwprogressbutton_percentage_text_view  更新 (210.8 MB)
time.sleep(5)
btn_progress = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_id("com.huawei.appmarket:id/hwprogressbutton_percentage_text_view"))
print(btn_progress.text)
# btn_progress = driver.find_element_by_id('com.huawei.appmarket:id/hwprogressbutton_percentage_text_view')
# print(btn_progress)

# try:
#     driver.find_element_by_id(id_='com.yuanding.seebaby:id/btn_update')
# except:
#     print('没有找到这个元素')
    
# webdriver.W
# weWebDriverWait(s)


#第二种#back_button = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']"))
# #back_button.click()
# #第三种#WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']")).click()
