from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\turnt\OneDrive\デスクトップ\Python\chromedriver.exe")
driver.get("https://www.google.co.jp/")

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()

for elem_h3 in driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3'):
    print(elem_h3.text)
    elem_a = elem_h3.find_element_by_xpath("..")
    print(elem_a.get_attribute("href"))