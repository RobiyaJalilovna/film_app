from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def hello_world(self):
        self.client.get('http://127.0.0.1:8000/films/')