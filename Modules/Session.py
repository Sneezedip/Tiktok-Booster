import uuid,requests,socket

class Session():
    def __init__(self,version):
        self.client_id = uuid.uuid4()
        self.version = version
        self.IP = self._get_ip()
    def send_heartbeat(self):
        try:
            requests.post(f"https://sneezedip.pythonanywhere.com/heartbeat?client_id={self.client_id}&version={self.version}&ip={self.IP}")
        except:
            pass
    def _get_ip(self):
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify=True)
        if response.status_code != 200:
            return 'Unable'
        data = response.json()
        return data['ip']


