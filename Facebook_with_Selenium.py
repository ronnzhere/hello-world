from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

user = "ronnzhere@gmail.com"
pwd = "mop200_24271987"
driver = webdriver.Chrome(executable_path='C:\\Users\\ron\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

if __name__ == '__main__':
    pass

