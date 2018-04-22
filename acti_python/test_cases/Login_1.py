from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append('C:\\Users\\luckie\Desktop\\acti_python')
from login.page_object import Login_page as lp
from login.common import Driver
# print(sys.path)

x= lp()

class Login():
	def login(self):
		Driver.driver(self).get('http://localhost:82/login.do;jsessionid=11eurcv87n3mm')
		x.userName().send_keys('admmin')
		x.password().send_keys('manager')
		x.submit().click()
x1 = Login()
x1.login()	