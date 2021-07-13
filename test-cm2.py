    from locust import HttpLocust, TaskSet, task
    from random import randint, randrange
    import time
    class UserTasks(TaskSet):
        @task
        def user_workflow(self):
            heartbeats = randint(2, 5) 
            print('number of heartbeats', heartbeats)
            self.client.get("/v2/metadata", auth=("ccc",""))
            init_session_response = self.client.post("/v2/sessions/test_mvpd/user_test", auth=("ccc",""))
            session_id = init_session_response.headers['Location']
            new_uri = "/v2/sessions/test_mvpd/user_test" + '/' + session_id
            print('location is ', session_id)
            for i in range(1, heartbeats):
                time.sleep(60)
                hb_response = self.client.post(new_uri, auth=("ccc",""))
                print(hb_response.content)
            del_session_response = self.client.post(new_uri, auth=("ccc",""))
            print(del_session_response.content)
        @task
        def stats(self):
            self.client.get("/")
    class WebsiteUser(HttpLocust):
        task_set = UserTasks
