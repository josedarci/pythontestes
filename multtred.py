from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading

def open_browser(url, iteration):
    print(f"Itera��o {iteration}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Aqui voc� pode adicionar qualquer l�gica adicional para interagir com a p�gina, se necess�rio

    # Fechar o navegador ap�s concluir as a��es
    driver.quit()

# URL de destino
url = "https://www.tiktok.com/@joserodriguesjr1975/video/7352868462038945030"

# Criar e iniciar threads
threads = []
for i in range(50):
    thread = threading.Thread(target=open_browser, args=(url, i+1))
    threads.append(thread)
    thread.start()

# Esperar todas as threads terminarem
for thread in threads:
    thread.join()
