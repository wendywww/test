from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/Users/uwangw7/PycharmProjects/SeleniumTest/drivers/chromedriver")
#driver = webdriver.Firefox("/Users/uwangw7/PycharmProjects/SeleniumTest/drivers/geckodriver")
#driver = webdriver.Ie()

#driver.set_page_load_timeout(10)


#go to the web page u want to test
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("PST time") #input in the box, find element by name (while inspect find the name as "q", send_keys as the input)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER) #click the buttons
#time.sleep(4)
driver.maximize_window()
driver.refresh()
driver.quit()
print("Test has completed successfully")