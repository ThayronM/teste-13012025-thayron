'''
Script criado para acessar o site da Cemig e pegar o valor da bandeira tarifária.
Apenas criei ele para armazenar as tarifas antes de jogar no código principal.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pg

# acessando o site da cemig
web = webdriver.Chrome()
web.get("https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/")
    
    
# resisdencial
# bandeira vermelha1   
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[4]')
# bandeira verde
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[2]')
# bandeira amarela
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[3]')

# comercial e industrial
# bandeira verde
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[2]')
# bandeira amarela
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[3]')
# bandeira vermelha1
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[4]')
# bandeira vermelha2
bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[5]')

print(bandeira.text)