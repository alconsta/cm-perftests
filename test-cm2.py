    from locust import HttpLocust, TaskSet, task
    class UserTasks(TaskSet):
        @task
        def index(self):
            self.client.get("/v2/metadata", auth=("ccc",""))
            response = self.client.post("/v2/sessions/test_mvpd/user_test")
            print("Respone body is: ", response)
            print(respone.content.decode().find('Location'))
        @task
        def stats(self):
            self.client.get("/")
    class WebsiteUser(HttpLocust):
        task_set = UserTasks
