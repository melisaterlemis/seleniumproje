from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.get('https://www.amazon.com.tr/')
browser.maximize_window()
cookie_button=browser.find_element(By.XPATH,'//*[@id="sp-cc-accept"]').click()
login_button=browser.find_element(By.XPATH,'//*[@id="nav-link-accountList"]/span').click()
email_input=browser.find_element(By.XPATH,'//*[@id="ap_email"]')
try:
 email_input.send_keys('devvmelisaa@gmail.com')
 email_input.send_keys(Keys.RETURN)
 time.sleep(5)

 password_input=browser.find_element(By.XPATH,'//*[@id="ap_password"]')
 password_input.send_keys('Melisa1234.')
 password_input.send_keys(Keys.RETURN)
 time.sleep(5)

 print('Test1: Başarılı giriş.')
except:
 print('Test1: Başarısız giriş.')

try:
 search_input=browser.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
 search_input.send_keys('kitap')
 search_input.send_keys(Keys.RETURN)
 time.sleep(5)
 print('Test2: Arama basarili.')
except:
 print("Test2: Arama basarisiz.")
 
try:
 kizil_veba=browser.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[3]/div[1]/h2/a/span').click()
 time.sleep(5)
 print('Test3: Kitap seçildi.')
except:
  print('Test3: Kitap seçilmedi.')

try:
 sepete_ekle_button=browser.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()
 time.sleep(5)
 sepet_button=browser.find_element(By.XPATH, '//*[@id="nav-cart-text-container"]').click()
 time.sleep(5)
 print('Test4: Sepete ekleme basarili.')
except:
 print('Test4: Sepete ekleme basarisiz.')

time.sleep(100)
#browser.quit()

 