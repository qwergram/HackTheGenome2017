from secrets import *
import requests
from requests.auth import HTTPBasicAuth
import requests_oauthlib

class OAuth2DummyClient(object):
    
    """
    Code mostly copied from here:
    http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#available-workflows
    """

    def __init__(self, app_id, app_secret, redirect_uri):
        
        assert redirect_uri.startswith("https://"), "redirect must be https://"
        
        self.app_id = app_id
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri

    def auto_run(self):
        self.setOAuth()
        self.setAuthUrl()
        self.setToken(input("Full auth_response: "))
        print(self.token)

    def setOAuth(self):
        self.oauth = requests_oauthlib.OAuth2Session(self.app_id, redirect_uri=self.redirect_uri)


    def setAuthUrl(self):
        self.auth_url, state = self.oauth.authorization_url(
            'https://sequencing.com/oauth2/authorize'
        )
        print("Auth URL:", self.auth_url)


    def setToken(self, auth_response):
        self.token = self.oauth.fetch_token(
            "https://sequencing.com/oauth2/token",
            authorization_response=auth_response,
            client_secret=self.app_secret
        )

    def get(self, url):
        return self.oauth.get(url)
    

def main():
    R = OAuth2DummyClient(
        client_id,
        client_secret,
        return_url
    )
    R.auto_run()


if __name__ == "__main__":
    main()