from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import xpath
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/v1/inventory.html')
driver.maximize_window()


# excel = pd.read_excel('')


driver.find_element(By.XPATH, xpath.FILTRO).click()
driver.find_element(By.XPATH, xpath.PRICE_LOW_HI).click()

inventario = driver.find_elements(By.XPATH, xpath.INVENTARIO)

for produto in inventario:
    elemento = produto.find_elements(By.TAG_NAME, "div")
    for div in elemento:
        botoes = div.find_elements(By.TAG_NAME, "button")
        for botao in botoes:
            if "9.99" in div.text:
                sleep(1)
                if "REMOVE" in div.text:
                    continue
                botao.click()
            else:
                continue


driver.find_element(By.XPATH, xpath.CARRINHO).click()
driver.find_element(By.XPATH, xpath.CHECKOUT).click()

sleep(1)
driver.find_element(By.XPATH, xpath.NOME).send_keys("Lucio")
sleep(1)
driver.find_element(By.XPATH, xpath.SOBRENOME).send_keys("Neto")
sleep(1)
driver.find_element(By.XPATH, xpath.ZIPCODE).send_keys("0000000")
sleep(1)
driver.find_element(By.XPATH, xpath.CONTINUAR_CHECKOUT).click()

driver.find_element(By.XPATH, xpath.FINISH).click()
sleep(1)
driver.quit()
print('oi')