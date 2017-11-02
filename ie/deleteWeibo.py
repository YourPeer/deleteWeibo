#-*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support import  expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# print u'请输入你的微博账号：'
# username=raw_input()
# print u'请输入你的微博密码：'
# password=raw_input()
#
# driver=webdriver.Ie(executable_path='IEDriverServer.exe')
# driver.get("http://weibo.com/login.php")
# time.sleep(3)
# elem=WebDriverWait(driver,10,0.5).until(lambda x: x.find_element_by_name("username"))
# elem.clear()
# elem.send_keys(username)
# elem=WebDriverWait(driver,10,0.5).until(lambda x: x.find_element_by_name("password"))
# elem.clear()
# elem.send_keys(password)
# button=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_class_name("btn_32px"))
# button.click()
# time.sleep(3)
# driver.get("http://weibo.com/2413243573/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1")
# time.sleep(3)
# # for i in range(0,5):
# #     a=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/a"))
# #     a.click()
# #     b=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a"))
# #     b.click()
# #     c=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/p[2]/a[1]"))
# #     c.click()
# for i in range(0,20):
#     try:
#         print u"正在删除第"+str(i+1)+u"条微博，请等待......"
#         a=driver.find_elements_by_css_selector('.screen_box a')
#         a1=a[0]
#         a1.click()
#         a2=WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_link_text("删除"))
#         a2.click()
#         a3 = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_link_text("确定"))
#         a3.click()
#         driver.refresh()
#         print u"删除第" + str(i + 1) + u"条微博成功！"
#         driver.implicitly_wait(10)
#     except:
#         print u"删除出错，正在重新刷新页面，请稍后......"
#         driver.refresh()
#         driver.implicitly_wait(10)
# driver.quit()
str1="http://weibo.com/u/2413243573/home?wvr=5&lf=reg"
str2=str1.split("u/")[1].split("/home")[0]
print str2