from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import sys
sys.path.append('C:\\Users\\luckie\Desktop\\acti_python')
from path_storage.path_storage_ import Paths_ as P

class Create_customer:
	def __init__(self, driver):
		self.driver = driver

	def click_tasks(self):
		self.tasks = self.driver.find_element(By.XPATH, P.tasks)
		return self.tasks

	def pro_and_cust_link(self):
			self.pro_and_cust = self.driver.find_element(By.XPATH, P.pro_and_cust)
			return self.pro_and_cust

	def create_cust_btn(self):
		self.create_cust_btn = self.driver.find_element(By.XPATH, P.create_cust_btn)
		return self.create_cust_btn

	def cust_name(self):
		self.cust_name = self.driver.find_element(By.XPATH, P.cust_name)
		return self.cust_name

	def cust_description(self):
		self.cust_description = self.driver.find_element(By.XPATH, P.cust_description)
		return self.cust_description

	def cust_created_btn(self):
		self.cust_created_btn = self.driver.find_element(By.XPATH, P.cust_created_btn)
		return self.cust_created_btn 
#about cust names
	def cust_names(self):
		self.cust_names = self.driver.find_elements(By.XPATH, P.customized_names)
		return self.cust_names
	# delete cust names
	def delete_cust(self):
		self.del_cust = self.driver.find_element(By.XPATH, P.delete_cust)
		return self.del_cust
	def confirm_delete(self):
		self.confirm_delete = self.driver.find_element(By.XPATH, P.confirm_delete)
		return self.confirm_delete

# this should to be taken to Users class 
	def  users_sec(self):
		self.users = self.driver.find_element(By.XPATH, P.users)
		return self.users
	def all_users(self):
		self.all_users =  self.driver.find_elements(By.XPATH, P.all_users)
		print(type(self.all_users))
		return self.all_users
# about settings
	def setting_click(self):
		self.setting_click = self.driver.find_element(By.XPATH, P.setting_icon)
		return self.setting_click
	def logo_and_color_scheme(self):
		self.logo_and_color_scheme = self.driver.find_element(By.XPATH, P.logo_and_color_scheme)
		return self.logo_and_color_scheme
	def links_inside_setting(self):
		# self.links = self.setting_click()
		pass
	def all_under_setting(self):
		self.all_under_setting = self.driver.find_elements(By.XPATH, P.all_under_setting)
		return self.all_under_setting	
# about add-ons 
	def add_ons_click(self):
		self.add_ons = self.driver.find_element(By.XPATH, P.add_ons_icon)
		return self.add_ons
	def all_under_add_ons(self):
		self.all_under_add_ons = self.driver.find_elements(By.XPATH, P.all_under_add_ons)
		return self.all_under_add_ons