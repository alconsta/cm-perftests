from locust import HttpLocust, TaskSet, task
from random import randrange, choices
import time, string
class UserTasks(TaskSet):
    def generate_subject(self):
        length = randrange(14, 38)
        subejctid = ''.join(choices(string.ascii_letters+string.digits+'-',k=length))
        return subejctid
    @task
    def user_workflow(self):
        heartbeats = randrange(2, 5)
        heartbeat_time = 10
        mvpd = "test_mvpd"
        userid = self.generate_subject()
        initial_uri = "/v2/sessions/" + mvpd + "/" + userid
        self.client.get("/v2/metadata", auth=("ccc",""))
        init_session_response = self.client.post(initial_uri, auth=("ccc",""))
        session_id = init_session_response.headers['Location']
        new_uri = initial_uri + '/' + session_id
        for i in range(1, heartbeats):
            time.sleep(heartbeat_time)
            hb_response = self.client.post(new_uri, auth=("ccc",""))
        time.sleep(heartbeat_time)    
        del_session_response = self.client.delete(new_uri, auth=("ccc",""))
class WebsiteUser(HttpLocust):
    task_set = UserTasks
