from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import sys 
sys.path.append('C:\\Users\\luckie\Desktop\\acti_python')
from path_storage.path_storage_ import Paths_ as P  
class Login():
	

	def __init__(self, driver):
		self.driver = driver 

	def get_username(self):
		self.username = self.driver.find_element(By.XPATH, P.username)
		return self.username

	def get_password(self):
		self.password = self.driver.find_element(By.XPATH, P.password)
		return self.password

	def  submit(self):
		self.submit = self.driver.find_element_by_xpath(P.submit)
		return self.submit