from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Configuração da espera explícita
wait = WebDriverWait(driver, 10)

# URL do formulário de cadastro
url = "https://www.linkedin.com/signup?_l=pt"

for i in range(10):
    driver.get(url)

    # Dados de teste
    email = f"teste_{i+1}@gmail.com" if i > 0 else "teste@gmail.com"
    password = "Senha123"
    first_name = "NomeTeste"
    last_name = "SobrenomeTeste"

    # Preencher os campos de e-mail e senha
    email_field = driver.find_element(By.ID, "email-or-phone")
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Clicar no botão "Continuar"
    continue_button = driver.find_element(By.ID, "join-form-submit")
    continue_button.click()

    # Preencher os campos de nome e sobrenome
    first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys(last_name)

    # Esperar e clicar no botão "Avançar"
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.artdeco-button")))
    next_button.click()

    # Adicione mais lógica e tempo de espera conforme necessário

driver.quit()
