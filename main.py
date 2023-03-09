from selenium import webdriver
from selenium.webdriver.common.by import By
from Search import Search
import time
import csv

#Para recopilar informacion de una marca en concreto
def TipoProductoMarca():
    pass


product = 'Varitas de merluza.'#"Refresco cola Coca-Cola 33cl pack 12 zero zero sin cafeína"



driver = webdriver.Chrome()



search = Search(product,driver)

#Obtenemos la informacion de los supermercados
Carrefour = search.CarrefourProduct()
# AHORRA MAS
# DIA
# ALDI
# MERCADONA
# EROSKI
# CORTE INGLES


ListaSupermercados = [Carrefour]



title_product = product.replace(" ", "_")


with open(f'salidas/{title_product}.csv', mode='w', newline='') as productos_csv:

    writer = csv.writer(productos_csv)
    

    for Supermercado in ListaSupermercados:
        writer.writerow(Supermercado)







time.sleep(5)
driver.quit()















def MostrarMercadona():
    pass


def MostrarAhorraMas():
    pass