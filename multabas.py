from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading

def open_browser(url, iteration):
    print(f"Itera��o {iteration}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Abrir a primeira aba com a URL desejada
    driver.get(url)

    # Abrir mais nove abas com a mesma URL
    for _ in range(9):
        driver.execute_script("window.open('');") # Abre uma nova aba
        driver.switch_to.window(driver.window_handles[-1]) # Muda o foco para a nova aba
        driver.get(url) # Carrega a URL na nova aba

    # Agora, o navegador tem 10 abas abertas com a mesma URL

    # L�gica adicional aqui, se necess�rio

    # Fechar o navegador ap�s concluir as a��es
    driver.quit()

# URL de destino
url = "https://open.spotify.com/search/Karla%20Hill"

# Criar e iniciar threads
threads = []
for i in range(50): # N�mero de navegadores a serem abertos
    thread = threading.Thread(target=open_browser, args=(url, i+1))
    threads.append(thread)
    thread.start()

# Esperar todas as threads terminarem
for thread in threads:
    thread.join()
