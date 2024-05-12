from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Intervalo entre as a��es de cada usu�rio simulado (entre 1 e 5 segundos)
    wait_time = between(1, 5)

    @task
    def view_homepage(self):
        # Acessa a p�gina inicial
        self.client.get("/")

    # Voc� pode adicionar mais tarefas para simular diferentes intera��es
    # @task
    # def view_other_page(self):
    #     # Exemplo: acessa outra p�gina do site
    #     self.client.get("/outra-pagina")
