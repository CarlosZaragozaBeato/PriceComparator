from selenium import webdriver
from selenium.webdriver.common.by import By
from Search import Search
import time
import csv


def guardarCSV(prd, listaProductos):
    title_product = prd.replace(" ", "_")

    with open(f'salidas/{title_product}.csv', mode='w', newline='') as productos_csv:

        writer = csv.writer(productos_csv)
        
        for Supermercado in listaProductos:
            writer.writerow(Supermercado)




products = ['Cacao soluble instantáneo Nestlé Nesquik sin gluten 390 g.',
            'Refresco cola Coca-Cola 33cl pack 12 zero zero sin cafeína',
            'Varitas de merluza Pescanova 450 g.',
            'ERRRORRERRORRERRRORRROERO']

driver = webdriver.Chrome()

driver.maximize_window()

for product in products:
    
    search = Search(product,driver)
    
    Carrefour = search.CarrefourProduct()
    AhorraMas = search.AhorraMasProduct()
    Dia = search.DiaProduct()

    ListaSupermercados = [Carrefour, AhorraMas,Dia]

    guardarCSV(product, ListaSupermercados)




time.sleep(2)
driver.quit()