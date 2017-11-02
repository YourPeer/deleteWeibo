#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
print u'请输入你的微博账号：'
username=raw_input()
print u'请输入你的微博密码：'
password=raw_input()
print u'请输入你要删除前几条微博：'
num=raw_input()
driver=webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("http://weibo.com/login.php")
time.sleep(3)
elem=WebDriverWait(driver,30,0.5).until(lambda x: x.find_element_by_name("username"))
elem.clear()
elem.send_keys(username)
elem1=WebDriverWait(driver,10,0.5).until(lambda x: x.find_element_by_name("password"))
elem1.clear()
elem1.send_keys(password)
elem2=driver.find_element_by_class_name("W_input")
if elem2.is_displayed():
    print u"请输入验证码:"
    w=raw_input()
    elem2.clear()
    elem2.send_keys(w)
    time.sleep(1)
button=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_class_name("btn_32px"))
button.click()
time.sleep(3)
url=driver.find_element_by_class_name('gn_name')
print(url)
driver.get(url.get_attribute("href"))
time.sleep(3)
# for i in range(0,5):
#     a=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/a"))
#     a.click()
#     b=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a"))
#     b.click()
#     c=WebDriverWait(driver,5,0.5).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/p[2]/a[1]"))
#     c.click()
for i in range(0,int(num)):
    try:
        print u"正在删除第"+str(i+1)+u"条微博，请等待......"
        a=driver.find_elements_by_css_selector('.screen_box a')
        a1=a[0]
        a1.click()
        a2=WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_link_text("删除"))
        a2.click()
        a3 = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_link_text("确定"))
        a3.click()
        driver.refresh()
        print u"删除第" + str(i + 1) + u"条微博成功！"
        driver.implicitly_wait(10)
    except:
        print u"删除出错，正在重新刷新页面，请稍后......"
        driver.refresh()
        driver.implicitly_wait(10)
driver.quit()
