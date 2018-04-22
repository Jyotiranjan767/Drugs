from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import sys 
sys.path.append('C:\\Users\\luckie\Desktop\\acti_python')
from page_objects.login_page import Login
from login.common import Driver
from login.common import Common_driver
from page_objects.create_cust import Create_customer as cc

x = Driver()
cd = Common_driver()
c = cc(x.driver())
print("e0qw9999999")

def login():
	xx =  Login(x.driver())
	x.driver().get('http://localhost:82/login.do;jsessionid=1ge0jq4fjskax')
	xx.get_username().send_keys("admin")
	xx.get_password().send_keys('manager')
	xx.submit().click()

######## tasks sections 
def tasks():
	x.driver().implicitly_wait(4)
	c.click_tasks().click()
	# cd.actions_double_click(c.click_tasks())
	# cd.explicit_wait(c.click_tasks())
	cd.actions_click(c.pro_and_cust_link())#.click()

def create_tasks():
	# c.create_cust_btn().click()
	cd.actions_click(c.create_cust_btn())
	c.cust_name().send_keys("luckie")
	c.cust_description().send_keys('she still looks that awesome after even so much of oragsms')
	c.cust_created_btn().click()

def delete_names():
	for cus  in c.cust_names():
		# print(cus.text.strip())
		cus1 = cus.find_elements_by_tag_name('a')
		for cus11 in cus1:
			x.driver().implicitly_wait(4)

			if 'luckie' == cus11.text.strip():
				cus11.click()
				c.delete_cust().click()
				# cd.actions_click(c.delete_cust())
				c.confirm_delete().click()
				# cd.actions_click(c.confirm_delete())
			else: print("you failed everybody who always cared for you")
###users sections
def about_users():
	x.driver().implicitly_wait(4)

	c.users_sec().click()
	# print(type(c.all_users()))
	for user in c.all_users():
		print(user.text)
		# print(user.tag_name)
		# print(user.parent)
		# print(user.location)
		# print(user.size)
# go and make some modifications in settings
def settings():
	# c.setting_click().click()
	cd.actions_click(c.setting_click())
def inside_setting():
	# cd.select_by_visible_text(c.setting_click(),'Logo & Color Scheme').click()
	cd.actions_move_to_element(c.setting_click(), c.logo_and_color_scheme())
def all_links_under_setitngs():
	for i, link in enumerate(c.all_under_setting()):
		print(link.text)

# go and make some modification in add-ons		
def click_add_ons():
	x.driver().implicitly_wait(4)
	# cd.actions_click(c.add_ons_click())
	c.add_ons_click().click()
def all_links_under_add_ons():
	x.driver().implicitly_wait(4)
	for i,link in enumerate(c.all_under_add_ons()):
		print(i, link.text)



login()

# tasks()

# for i in range(3):
print('jyoti    e9w0e4')
# create_tasks()
# delete_names()
settings()
inside_setting()
# sleep(2000)
# all_links_under_setitngs()	
click_add_ons()
all_links_under_add_ons()