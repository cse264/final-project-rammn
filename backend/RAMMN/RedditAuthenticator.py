# Library for making HTTP requests
from email import header
import requests
import requests.auth

from RAMMN.ExternalAPIAuthenticator import ExternalAPIAuthenticator
# from RAMMN import cache


class RedditAuthenticator(ExternalAPIAuthenticator):
    '''
    The Reddit Authenticator is used to wrap any Reddit user related OAuth activity.\n
    General API information: https://github.com/reddit-archive/reddit/wiki/OAuth2.\n
    Python example code: https://github.com/reddit-archive/reddit/wiki/OAuth2-Python-Example.
    '''

    def __init__(self, secerts) -> None:
        '''
        Construct new Reddit Authenticator instance.\n
        Must have "REDDIT_OAUTH_CLIENT_ID" and "REDDIT_OAUTH_CLIENT_SECRET" config variables set.
        '''
        super().__init__(secerts)

        if ('CLIENT_ID' not in self._secerts["REDDIT_OAUTH"]) or ('CLIENT_SECERT' not in self._secerts["REDDIT_OAUTH"]) or ('REDIRECT_URI' not in self._secerts["REDDIT_OAUTH"]):
            raise ValueError(self._secerts)

        self.__user_agent = "RAMMN:v0.1 (by /u/TheArmageddon18"

    def make_authorization_url(self):

        # Note: this number should be randomized in the future
        from uuid import uuid4
        state = 6  # str(uuid4())

        # cache.set(state, "valid")

        params = {"client_id": self._secerts["REDDIT_OAUTH"]["CLIENT_ID"],
                  "response_type": "code",
                  "state": state,
                  "redirect_uri": self._secerts["REDDIT_OAUTH"]["REDIRECT_URI"],
                  "duration": "temporary",
                  "scope": "identity"}
        import urllib.parse
        url = "https://ssl.reddit.com/api/v1/authorize?" + \
            urllib.parse.urlencode(params)
        return url

    def get_token(self, code):
        headers = {"User-Agent": self.__user_agent}
        client_auth = requests.auth.HTTPBasicAuth(
            self._secerts["REDDIT_OAUTH"]["CLIENT_ID"], self._secerts["REDDIT_OAUTH"]["CLIENT_SECERT"])
        post_data = {"grant_type": "authorization_code",
                     "code": code,
                     "redirect_uri": self._secerts["REDDIT_OAUTH"]["REDIRECT_URI"]}
        response = requests.post("https://ssl.reddit.com/api/v1/access_token",
                                 headers=headers,
                                 auth=client_auth,
                                 data=post_data)
        token_json = response.json()
        return token_json["access_token"]

    def get_user(self, access_token):
        headers = {"Authorization": "bearer " + access_token,
                   "User-Agent": self.__user_agent}
        response = requests.get(
            "https://oauth.reddit.com/api/v1/me", headers=headers)
        user_json = response.json()
        return user_json

    def validate_credentials() -> bool:
        '''
        Check if the credentials are correct with Reddit.\n
        Returns dictionary of user information if verification is successful, otherwise the value 'None'.
        '''
        pass
