from flask import current_app, g

# Library for making HTTP requests
import requests
import requests.auth


class ExternalAPIAuthenticator:
    '''
    External API authenticator handles any OAuth functionality.\n
    I.e: token validation, payload information, etc.\n
    '''

    def __init__(self) -> None:
        '''
        Create an external API authenticator.\n
        Each implementation subclass may have unique requirements of what secerts exist.\n
        If no secerts are added, then an error will be thrown.\n
        Adding malformed secerts will result in HTTP request errors.
        '''

        if(not current_app.config):
            raise ValueError(current_app.config)

        self.__secerts = current_app.config.copy()
        '''secerts hold any API key information needed by the authenticator'''

    def set_secerts(self, dict) -> None:
        '''
        Set the external API secert for future calls.\n
        Invalid secerts may throw HTTP request related errors.\n
        Returns 'None'.'''
        self.__secerts = dict
        return

    def validate_credentials() -> bool:
        '''
        Validate a user at an external API using provided credentials.\n
        Returns true if the user is positvely confirmed by external API, false otherwise.
        '''
        pass


class RedditAuthenticator(ExternalAPIAuthenticator):
    '''
    The Reddit Authenticator is used to wrap any Reddit user related OAuth activity.\n
    General API information: https://github.com/reddit-archive/reddit/wiki/OAuth2.\n
    Python example code: https://github.com/reddit-archive/reddit/wiki/OAuth2-Python-Example.
    '''

    def __init__(self) -> None:
        '''
        Construct new Reddit Authenticator instance.\n
        Must have "REDDIT_OAUTH_CLIENT_ID" and "REDDIT_OAUTH_CLIENT_SECRET" config variables set.
        '''
        super().__init__()

        if ("REDDIT_OAUTH_CLIENT_ID" not in self.__secerts) or ("REDDIT_OAUTH_CLIENT_SECRET" not in self.__secerts) or ("REDDIT_OAUTH_REDIRECT_URI" not in self.__secerts):
            raise ValueError(self.__secerts)

    def make_authorization_url(self):

        # Note: this number should be randomized in the future
        state = 5

        params = {"client_id": self.__secerts["REDDIT_OAUTH_CLIENT_ID"],
                  "response_type": "code",
                  "state": state,
                  "redirect_uri": self.__secerts["REDDIT_OAUTH_REDIRECT_URI"],
                  "duration": "temporary",
                  "scope": "identity"}
        import urllib
        url = "https://ssl.reddit.com/api/v1/authorize?" + \
            urllib.urlencode(params)
        return url

    def get_token(self, code):
        client_auth = requests.auth.HTTPBasicAuth(
            self.__secerts["REDDIT_OAUTH_CLIENT_ID"], self.__secerts["REDDIT_OAUTH_CLIENT_SECERT"])
        post_data = {"grant_type": "authorization_code",
                     "code": code,
                     "redirect_uri": self.__secerts["REDDIT_OAUTH_REDIRECT_URI"]}
        response = requests.post("https://ssl.reddit.com/api/v1/access_token",
                                 auth=client_auth,
                                 data=post_data)
        token_json = response.json()
        return token_json["access_token"]

    def get_username(self, access_token):
        headers = {"Authorization": "bearer " + access_token}
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
        me_json = response.json()
        return me_json['name']

    def validate_credentials() -> bool:
        '''
        Check if the credentials are correct with Reddit.\n
        Returns dictionary of user information if verification is successful, otherwise the value 'None'.
        '''
        pass


class AuthenticatorFactory:

    def __init__(self, option):
        '''
        In the request lifetime, the authenticator is created once!\n
        In case the secerts need to be changed after authenticator construction, use ExternalAPIAuthenticator.set_secerts()
        '''
        self.__authenticators = {"REDDIT": RedditAuthenticator}
        if option in self.__authenticators:

            if self.__authenticators not in g:
                g[self.__authenticators] = self.__authenticators[option]()
            
            return g[self.__authenticators]

        else:
            raise ValueError(option)

    def get_options(self):
        return self.__authenticators.keys()

    def _authenticate_with_reddit():
        pass
