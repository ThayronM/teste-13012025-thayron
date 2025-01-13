from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pyautogui as pg

def calculadora(consumo: list, classe: str, bandeira: str) -> tuple:
    """
    retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """
    economia_anual = 0
    economia_mensal = 0
    desconto_aplicado = 0
    cobertura = 0

    # Desenvolva seu código aqui #
    
    # acessando o site da cemig
    web = webdriver.Chrome()
    web.get("https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/")

    # média de consumo
    media_consumo = sum(consumo) / len(consumo)
    # print(media_consumo)
    
    # economia residencial
    if classe == "Residencial":
        if bandeira == "BANDEIRA VERDE":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[2]')
        if bandeira == "BANDEIRA AMARELA":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[3]')
        if bandeira == "BANDEIRA VERMELHA 1":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr/td[4]')
        
        if media_consumo < 10000:
            desconto_aplicado = 0.18
            cobertura = 0.90   
        elif media_consumo >= 10000 and media_consumo <= 20000:
            desconto_aplicado = 0.22
            cobertura = 0.95  
        else:
            desconto_aplicado = 0.25
            cobertura = 0.99
            
        
    # economia comercial
    elif classe == "Comercial":
        if bandeira == "BANDEIRA VERDE":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[2]')
        if bandeira == "BANDEIRA AMARELA":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[3]')
        if bandeira == "BANDEIRA VERMELHA 1":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[4]')
        if bandeira == "BANDEIRA VERMELHA 2":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[5]')

        if media_consumo < 10000:
            desconto_aplicado = 0.16
            cobertura = 0.90    
        elif media_consumo >= 10000 and media_consumo <= 20000:
            desconto_aplicado = 0.18
            cobertura = 0.95
        else:
            desconto_aplicado = 0.22
            cobertura = 0.99
            
            
    # economia industrial
    elif classe == "Industrial":
        if bandeira == "BANDEIRA VERDE":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[2]')
        if bandeira == "BANDEIRA AMARELA":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[3]')
        if bandeira == "BANDEIRA VERMELHA 1":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[4]')
        if bandeira == "BANDEIRA VERMELHA 2":
            bandeira = web.find_element(By.XPATH, '//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr/td[5]')
            
        if media_consumo < 10000:
            desconto_aplicado = 0.12
            cobertura = 0.90
        elif media_consumo >= 10000 and media_consumo <= 20000:
            desconto_aplicado = 0.15
            cobertura = 0.95    
        else:
            desconto_aplicado = 0.18
            cobertura = 0.99
          
    # bandeira para float
    bandeira = float(bandeira.text.replace(",", "."))
    economia_anual = cobertura * media_consumo * bandeira * 12 * desconto_aplicado 
    economia_mensal = economia_anual / 12
        
        
    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura, 2),
    )


if __name__ == "__main__":
    print("Testando...")

    assert calculadora([1518, 1071, 968], "Industrial", "BANDEIRA VERMELHA 2") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    ) 

    assert calculadora([1000, 1054, 1100], "Residencial", "BANDEIRA VERMELHA 1") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )

    assert calculadora([973, 629, 726], "Comercial", "BANDEIRA AMARELA") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )

    assert calculadora([15000, 14000, 16000], "Industrial", "BANDEIRA VERMELHA 1") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )

    assert calculadora([12000, 11000, 11400], "Residencial", "BANDEIRA VERDE") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )

    assert calculadora([17500, 16000, 16400], "Comercial", "BANDEIRA AMARELA") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )

    assert calculadora([30000, 29000, 29500], "Industrial", "BANDEIRA VERMELHA 1") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )

    assert calculadora([22000, 21000, 21400], "Residencial", "BANDEIRA AMARELA") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )

    assert calculadora([25500, 23000, 21400], "Comercial", "BANDEIRA VERDE") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )

    print("Todos os testes passaram!")
    