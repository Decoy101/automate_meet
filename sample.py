# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def Glogin(mail_address, password):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element_by_xpath(
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def turnOffMicCam():
	mic = driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
	mic.click()
	driver.implicitly_wait(10)
	cam = driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
	cam.click()
	driver.implicitly_wait(10)


def joinNow():
	# Join meet
	join = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
	join.click()



# assign email id and password
mail_address = 'example@gmail.com'
password = 'abcd1234'

# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

# login to Google account
Glogin(mail_address, password)

# go to google meet
driver.get('https://meet.google.com/ffk-nhki-nwp')
turnOffMicCam()
joinNow()

