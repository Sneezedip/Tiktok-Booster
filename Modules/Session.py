import uuid,requests

class Session():
    def __init__(self,version):
        self.client_id = uuid.uuid4()
        self.version = version
    def send_heartbeat(self):
        try:
            requests.post(f"https://sneezedip.pythonanywhere.com/heartbeat?client_id={self.client_id}&version={self.version}")
        except:
            pass
