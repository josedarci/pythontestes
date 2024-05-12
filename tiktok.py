from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# URL do v�deo TikTok
url_tiktok = "https://www.linkedin.com/in/josedarci/"

for i in range(10):
    print(f"Iteracao {i + 1}")

    # Inicia o driver do Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vai para a URL do v�deo
    driver.get(url_tiktok)

    try:
        # Espera at� que o elemento com o texto "Continuar como convidado" seja carregado e clic�vel
        # Nota: Este seletor XPath � um exemplo e pode precisar de ajustes
        botao_convidado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Continuar como convidado')]"))
        )
        # Clica no elemento
        botao_convidado.click()

    except TimeoutException:
        print("Elemento 'Continuar como convidado' n�o encontrado ou a p�gina n�o foi carregada corretamente.")

    # Fecha o navegador
    driver.quit()
