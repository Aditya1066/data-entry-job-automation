from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

url = ("https://housing.com/rent/withoutbrokerage-flats-for-rent-in-jaipur-rajasthan-D2P268dw8h2rtw7ykpy?psafe_param=1&g"
       "ad_source=1&gclid=CjwKCAjwjsi4BhB5EiwAFAL0YIq7oC3s2surY6zCRoSBXSL1CfkKYsoSd59wEY9irxG2h8CRGGR1jhoCTAYQAvD_BwE")

form_url = "https://forms.gle/p2fFBnKRwVMkaCVh6"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
listings = soup.find_all("div", {"data-q": "result-data"})
links = []
prices = []
locations = []

for l in listings:
       links.append("https://housing.com"+l.find("a").get("href"))
       prices.append(l.find("div", {"data-q": "price"}).text)
       location = l.find("div", {"class": "T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title"}).text.split("in ", 1)
       locations.append(location[1])


print(links)
print(prices)
print(locations)

driver.get(form_url)

for i in range(len(listings)):
    time.sleep(2)
    print(f"Filling form number {i+1}")

    loc_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    loc_field.send_keys(locations[i])

    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(prices[i])

    link_field = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    time.sleep(2)

    another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()


