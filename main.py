from selenium import webdriver
from selenium.webdriver.common.by import By
from Search import Search
import time
import csv

#Para recopilar informacion de una marca en concreto
def TipoProductoMarca():
    pass


product = 'Cacao soluble instantáneo Nestlé Nesquik sin gluten 390 g.'
#'Refresco cola Coca-Cola 33cl pack 12 zero zero sin cafeína'
#'Varitas de merluza Pescanova 450 g.'




driver = webdriver.Chrome()

search = Search(product,driver)

#Obtenemos la informacion de los supermercados
Carrefour = search.CarrefourProduct()
AhorraMas = search.AhorraMasProduct()
Dia = search.DiaProduct()
# MERCADONA




# CREACIÓN DE CSV
ListaSupermercados = [Carrefour, AhorraMas,Dia]

title_product = product.replace(" ", "_")


with open(f'salidas/{title_product}.csv', mode='w', newline='') as productos_csv:

    writer = csv.writer(productos_csv)
    

    for Supermercado in ListaSupermercados:
        writer.writerow(Supermercado)

time.sleep(5)
driver.quit()