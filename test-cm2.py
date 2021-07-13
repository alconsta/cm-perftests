    from locust import HttpLocust, TaskSet, task
    from random import randint, randrange

    class UserTasks(TaskSet):
        @task
        def user_workflow(self):
            heartbeats = randint(5, 100)        
            self.client.get("/v2/metadata", auth=("ccc",""))
            response = self.client.post("/v2/sessions/test_mvpd/user_test", auth=("ccc",""))
            location = response.headers['Location']
            new_uri = "/v2/sessions/test_mvpd/user_test" + '/' + location
            print('location is ', location)
            for i in range(heartbeats):
                hb_response = self.client.post("/v2/sessions/test_mvpd/user_test", auth=("ccc",""))
                print(hb_response.content)
        @task
        def stats(self):
            self.client.get("/")
    class WebsiteUser(HttpLocust):
        task_set = UserTasks
