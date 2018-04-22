from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('C:\\Users\\luckie\Desktop\\acti_python')
print(sys.path)
from login.common import Driver 

class Login_page():
	def FindBy(by, value):
		# def decorator(func):
		def wrapper(self):
			return Driver.driver(self).find_element(by, value)
			# return wrapper
		return decorator
	@FindBy(By.NAME,'username')
	def userName():pass
	@FindBy(By.NAME, 'pwd')
	def password():pass
	@FindBy(By.XPATH, "//input[@type='submit']")
	def submit():pass
# class Login_page():
# 	# binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\Firefox.exe')

# 	def __init__(self):
# 		self.driver = webdriver.Chrome('C:\\Users\\luckie\\Downloads/chromedriver.exe') #Firefox() #(firefox_binary=binary)

# 	@FindBy(By.NAME, 'q')
# 	def search_input(self):pass
# 	def test_search(self):
# 		# self.driver=webdriver.Firefox()
# 		# print(type(self.search_input()))
# 		self.driver.get('https://www.google.co.in/')
# 		search = self.search_input()
# 		search.send_keys('selenium python')
# 		search.submit()
# 	def sdkj(self):
# 		print(type(self.search_input()))
# x = Login_page()
# # print(type(search_input())
# x.test_search()
# # x.sdkj()	