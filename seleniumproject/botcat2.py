from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")




driver1.get("https://www.youtube.com/watch?v=ZfRuhMAV1qA")




while True:
    sleep(20)
    driver1.refresh()


