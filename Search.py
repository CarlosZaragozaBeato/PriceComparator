from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Search:
    product_name = ""


    def __init__(self, product_name:str, driver):
        self.product_name = product_name
        self.driver = driver



    #BUSCAR EN CARREFOUR
    def CarrefourProduct(self):
        self.driver.get('https://www.carrefour.es/?gclid=Cj0KCQiAgaGgBhC8ARIsAAAyLfHJZAkh3PZU6zJ6jhoAhxnOvsCcPahmWyNHF4xUuQiT2F9gBk3rdloaAkgGEALw_wcB&gclsrc=aw.ds')
        
        btn_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        btn_cookies.click()

        #A la hora de buscar hay dos inputs diferentes el segundo se crea cuando clickamos el primero
        input_text_search_parent = self.driver.find_element(By.XPATH, '//*[@id="search-input"]')
        input_text_search_parent.click()
        
        #Introducimos el texto en el segundo input
        input_text_search_child = self.driver.find_element(By.XPATH, '//*[@id="empathy-x"]/header/div[1]/div/input[3]')
        input_text_search_child.send_keys(self.product_name)

        #Vamos a los productos 
        button_submit = self.driver.find_element(By.XPATH, '//*[@id="empathy-x"]/header/div/button[1]')
        button_submit.click()

        time.sleep(1)

        #Cojemos la informacion del producto
        price = self.driver.find_element(By.XPATH, '//*[@id="ebx-grid"]/article[1]/div/p/strong')
        return ('Carrefour',price.text[: -1].replace(' ', ''))





    #BUSCAR EN AHORRA MAS
    def AhorraMasProduct(self):
        self.driver.get('https://www.ahorramas.com/')

        time.sleep(1)
        
        btn_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        btn_cookies.click()

        #Introducimos el producto
        #Accedo a traves de la clase porque introduciendo el XPATH no tenia acceso a el.
        input_text = self.driver.find_element(By.CLASS_NAME, 'search-field') 
        input_text.click()
        input_text.send_keys(self.product_name)

        search_button = self.driver.find_element(By.CLASS_NAME, 'fa-search')
        search_button.click()

        price = self.driver.find_element(By.XPATH, '//*[@id="product-search-results"]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div/span/span')

        return ('Ahorra Mas',price.text[: -1].replace(' ', ''))



