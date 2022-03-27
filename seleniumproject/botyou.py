from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver5 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver1.get("https://www.youtube.com/watch?v=cfL1fZi5JeI")
driver2.get("https://www.youtube.com/watch?v=cfL1fZi5JeI")
driver3.get("https://www.youtube.com/watch?v=cfL1fZi5JeI")
driver4.get("https://www.youtube.com/watch?v=cfL1fZi5JeI")
driver5.get("https://www.youtube.com/watch?v=cfL1fZi5JeI")

while True:
    sleep(20)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
    driver5.refresh()
