from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # Abrir navegador maximizado
options.add_argument("--log-level=3")  # Ignorar avisos

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

input = driver.find_element(By.NAME, "q")
input.send_keys("GEFORCE RTX 4090")
input.send_keys(Keys.ENTER)

link = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[14]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div")
link.click()

description = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div[4]/div/div/div/p")
print(description.text)

# sleep(10)

driver.quit()
