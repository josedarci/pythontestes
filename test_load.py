import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url, index):
    try:
        response = requests.get(url)
        print(f"Requisição {index}: URL: {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Requisição {index}: Error accessing {url}: {e}")

def main():
    url = "https://www.choqueifofoca.com.br/feeds/posts/default"
    num_requests = 1000  # Número de requisições

    print("Iniciando requisições...")

    # Usando ThreadPoolExecutor para fazer requisições concorrentes
    with ThreadPoolExecutor(max_workers=40) as executor:
        tasks = [executor.submit(fetch_url, url, i) for i in range(1, num_requests + 1)]
        for future in tasks:
            future.result()  # Aguarda a conclusão de cada tarefa

if __name__ == "__main__":
    main()
