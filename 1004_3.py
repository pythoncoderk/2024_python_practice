from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./chromedriver.exe")

browser.get("https://www.yahoo.com/")
assert ("Yahoo" in browser.title)

elem = browser.find_element_by_name("p")
elem.send_keys("sleniumhq" + Keys.RETURN)

browser.quit()