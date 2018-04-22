
class Paths_:

	#login page 

	username  = "//*[@id='username']"
	password  = "//*[@id='loginFormContainer']/tbody/tr[1]/td/table/tbody/tr[2]/td/input"
	submit  = '//a[@id="loginButton"]/div'

	# from task  create customer 
	
	tasks  =  '//*[@id="topnav"]/tbody/tr[1]/td[3]/a' 
	pro_and_cust = '//*[@id="topnav"]/tbody/tr[2]/td/div[3]/a'
	create_cust_btn = '//*[@id="ext-comp-1002"]/span'

	cust_name = '//*[@id="customerLightBox_nameField"]'
	cust_description = '//*[@id="customerLightBox_descriptionField"]'
	cust_created_btn = '//*[@id="customerLightBox_commitBtn"]'

	cust_name_specified = '//*[@id="customerNameCell3"]/table/tbody/tr/td'
	customized_names = '//*[@id="customersProjectsForm"]/table/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr'
	delete_cust = '//*[@id="customerLightBox_deleteBtn"]/div/span'
	confirm_delete  = '//*[@id="operationConfirmDialogDiv"]/div/table/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/input'
	# users
	users = '//*[@id="topnav"]/tbody/tr[1]/td[5]/a'
	all_users =  '//*[@id="userListTableContainer"]/table/tbody/tr/td/table/tbody/tr/td/div/span'

	# setting sections
	setting_icon = '//*[@id="topnav"]/tbody/tr[1]/td[6]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/div[1]/div/div[1]/div[1]/div'
	logo_and_color_scheme = '//*[@id="popup_menu_item_7"]/a'
	
	all_under_setting = '//*[@id="popup_menu_items_content"]/li'

	#add-ons
	add_ons_icon = '//*[@id="topnav"]/tbody/tr[1]/td[6]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/div[2]/div/div[1]/div[1]'
	all_under_add_ons = '//*[@id="popup_menu_addons"]/div[2]/div/ul/li'	
