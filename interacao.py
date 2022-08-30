from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


chromedrive_path = 'C:/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
sleep(2)
webdriver.get('https://news.ycombinator.com/submit')
sleep(2)

usuario = webdriver.find_element(By.NAME, 'acct')
usuario.send_keys('davillops')
senha = webdriver.find_element(By.NAME, 'pw')
senha.send_keys('*****')

button_login = webdriver.find_element(By.CSS_SELECTOR, 'body > form:nth-child(6) > input[type=submit]')
button_login.click()
sleep(2)

url = 'https://news.ycombinator.com/'
webdriver.get(url)
entrarPag = webdriver.find_element(By.CLASS_NAME, 'titlelink')
entrarPag.click()
sleep(1)
