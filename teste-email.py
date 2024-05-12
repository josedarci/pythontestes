import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Obter o caminho absoluto para o arquivo de imagem
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'surfista.jpeg')

# Inicializa o WebDriver com webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL do formulário
url = 'https://josedarci.com/envia-email-com-anexo-phpmailer'

# Abrir a URL
driver.get(url)

# Esperar que a página carregue completamente
time.sleep(2)

# Loop para enviar o formulário 10 vezes
for i in range(1, 11):
    # Preencher o formulário
    name_input = driver.find_element(By.ID, 'name')
    name_input.clear()
    name_input.send_keys('José Darci')

    email_input = driver.find_element(By.ID, 'email')
    email_input.clear()
    email_input.send_keys('juniorinternet@gmail.com')

    subject_input = driver.find_element(By.ID, 'subject')
    subject_input.clear()
    subject_input.send_keys(f'Teste de Envio #{i}')

    message_input = driver.find_element(By.ID, 'message')
    message_input.clear()
    message_input.send_keys('Este é um teste de envio de formulário com anexo usando Selenium.')

    # Enviar arquivo - agora usando o caminho absoluto
    file_input = driver.find_element(By.ID, 'fileUpload')
    file_input.send_keys(image_path)  # Usando o caminho absoluto

    # Encontrar e clicar no botão de envio
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # Aguardar 1 segundo antes de repetir ou finalizar
    time.sleep(1)

    # Recarregar a página para resetar o formulário
    driver.refresh()

# Fechar o navegador após o loop
driver.quit()
