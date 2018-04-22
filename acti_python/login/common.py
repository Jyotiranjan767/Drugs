from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
class Driver():
	'''just for test testing purpose , real purpose has not been imple\
		mented yet.'''
	def __init__(self):pass
	flag1 = True
	@classmethod
	def driver(cls):
		if Driver.flag1:
			cls.driver1 = webdriver.Chrome('C:\\Users\\luckie\\Downloads/chromedriver_win32/chromedriver.exe')
			# cls.driver1 = webdriver.Ie('C:\\Users\\luckie\\Downloads/Compressed/IEDriverServer.exe')
			# cls.driver1 = webdriver.Firefox()#(executable_path = '')
			cls.driver1.maximize_window()
			Driver.flag1  = False	
		return cls.driver1
		# else : print('kro')
x = Driver()
class Common_driver():
	# de
	def __init__(self, webElement_for_select = None):  
		self.act = webdriver.ActionChains(Driver().driver())
		self.alt = Alert(Driver.driver())
		# self.select = Select(webElement_for_select)
	def explicit_wait(self, xpath):
		# self.wait = WebDriverWait(Driver().driver(), 10).until(EC.presence_of_element_located((xpath)))
		pass
		# return self.wait


	# use ActionChains class for clicking through action	
	def actions_click(self, menu):
		# self.act.move_to_element(menu)
		self.act.move_to_element(menu).click().perform()
		# self.act.click(menu)
		# self.act.perform()
	def actions_double_click(self, menu):
		self.act.double_click(menu).perform()
	def actions_move_to_element(self, menu, hidden_menu):
		self.act.move_to_element(menu).click().perform()
		self.act.click(hidden_menu).perform()
		# self.act.perform()

	#ActionChains for click and hold 
	def click_and_hold(self, webElement1):
		# act = ActionChains(Driver().driver())
		self.act.click_and_hold(webElement1).perform()

	#context click 
	def context_click(self, webElement1):
		self.act.context_click(webElement1).perform()
	#drag and drop
	def drag_and_drop(self, webElement1_drag, webElement1_drop):
		self.act.drag_and_drop(webElement1_drag, webElement1_drop).perform()  
	# key down
	def key_down(self, value ):
		self.act.key_down(Keys.CONTROL).send_keys(value).key_up(Keys.CONTROL).perform()
		#suppose you want to write ctrl+c , then put 'c' in value

	#Alerts  -  use this class to interact with alert prompts . It contains methods 
	# for dismissing ,accepting, and getting text from alert prompts
	
	# accepting 
	#accept the accept available
	def alert_accept(self):
		self.alt.accept()  # confirm a alert dialog 
	def alert_dismiss(self):
		self.alt.dismiss(self)
	# authenticate the username and password
	def alert_authenticate(self, username, password):
		Driver().driver().swith_to_alert.authenticate(username, password)
	def alert_send_keys(self, keys_to_send):
		self.alt.send_keys(keys_to_send)

	#text - to get text from alert
	# here is end of the alert
	@classmethod
	def sele(cls, webElement1):
		sel = Select(webElement1)
		return cls(sel)
	# select starts
	def select_by_index(self,webElement1, index):
		self.sel = Select(webElement1)
		# self.sel = Common_driver.sele(webElement1)
		self.sel.select_by_index(index)
	def select_by_visible_text(self, webElement1, text):
		self.sel = Select(webElement1)
		self.sel.select_by_visible_text(text)
	def select_by_value(self, webElement1):
		self.sel = Select(webElement1)
		self.sel.select_by_value(value)
