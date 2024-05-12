from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura��o do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL do formul�rio
url = "https://www.cigam.com.br/busca-paga?utm_source=google_ads&utm_medium=p.max&utm_campaign=sao_paulo&gad_source=1&gclid=CjwKCAjwwr6wBhBcEiwAfMEQs-_HTH5ZK8dCAMYdPmK4K6f-4EZ84d4_mnHcEV44tZ7FVDurwixf5RoCbTEQAvD_BwE"

for i in range(2):
    driver.get(url)

    # Gerar dados de usu�rio
    nome = f"Usuario {i+1}"
    telefone = "(55) 987654321"
    email = f"teste_{i+1}@gmail.com"
    funcionarios = "100"
    mensagem = "Buscando informa��es sobre o produto."

    # Preencher o formul�rio
    driver.find_element(By.ID, "form-input-nome").send_keys(nome)
    driver.find_element(By.ID, "form-input-telefone").send_keys(telefone)
    driver.find_element(By.ID, "form-input-email").send_keys(email)
    driver.find_element(By.ID, "form-input-funcionarios").send_keys(funcionarios)
    driver.find_element(By.ID, "form-input-mensagem").send_keys(mensagem)

    # Marcar checkbox
    checkbox = driver.find_element(By.ID, "form-input-consentimento-1")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(100)
    # Clicar no bot�o "Solicitar"
    driver.find_element(By.ID, "form-cabecalho-botao").click()

    # Esperar um pouco antes da pr�xima itera��o
    time.sleep(10)  # Ajuste este tempo conforme necess�rio

driver.quit()
