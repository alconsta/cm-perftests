    from locust import HttpLocust, TaskSet, task
    class UserTasks(TaskSet):
        @task
        def index(self):
            self.client.get("/v2/metadata", auth=("ccc",""))
            response = self.client.post("/v2/sessions/test_mvpd/user_test", auth=("ccc",""))
            location = response.headers['Location']
            print('location is ', location )
        @task
        def stats(self):
            self.client.get("/")
    class WebsiteUser(HttpLocust):
        task_set = UserTasks
