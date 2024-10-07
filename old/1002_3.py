import requests
from bs4 import BeautifulSoup

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

req = requests.get(url)

# print(req.text)

soup = BeautifulSoup(req.text, "lxml")
# print(soup.prettify())
print(soup.h2)