from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def obtener_productos_condis(max_productos=20):
    options = Options()
    options.add_argument("--headless")  # no browser window
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Change this if your chromedriver lives somewhere else
    service = Service("/usr/local/bin/chromedriver-mac-arm64/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://shop.condisline.com/store/condisline/ca/category/VERDURA-I-FRUITA")

    time.sleep(5)  # give the page time to load, TODO: switch to explicit waits

    productos = []

    cards = driver.find_elements(By.CLASS_NAME, "product-card__content")

    for card in cards[:max_productos]:
        try:
            nombre = card.find_element(By.CLASS_NAME, "product-card__title").text.strip()
            precio = card.find_element(By.CLASS_NAME, "product-price__final-price").text.strip()
            productos.append({
                "nombre": nombre,
                "precio": precio
            })
        except:
            continue

    driver.quit()
    return productos
