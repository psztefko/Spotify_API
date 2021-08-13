from env import CLIENT_ID, CLIENT_SECRET
import base64
import requests
import datetime


class Authorization():
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET

    def get_client_credentials(self):
        """Returns base64 encoded string"""

        if self.client_id == None or self.client_secret == None:
            raise Exception("You must set client_id and client_secret")
        client_creds_b64 = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        req = requests.post(self.token_url, data=self.get_token_data(), headers=self.get_token_headers())

        if req.status_code not in range(200, 299):
            return False

        data = req.json()
        now = datetime.datetime.now()
        self.access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = self.access_token_expires < now
        return True

