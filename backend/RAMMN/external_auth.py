class ExternalAPIAuthenticator:
    '''
    External API authenticator handles any OAuth functionality.\n
    I.e: token validation, payload information, etc.\n
    '''
    def __init__(self, secerts=None) -> None:
        '''
        Create an external API authenticator.\n
        Each implementation subclass may have unique requirements of what secerts exist.\n
        If no secerts are added, then an error will be thrown.\n
        Adding malformed secerts will result in HTTP request errors.
        '''

        if(not secerts):
            raise ValueError(secerts)

        
        self.__secerts = secerts
        '''secerts hold any API key information needed by the authenticator'''

        self.__secerts
    
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
    def __init__(self, secerts=None) -> None:
        '''
        Construct new Reddit Authenticator instance.\n
        Must have "REDDIT_OAUTH_CLIENT_ID" and "REDDIT_OAUTH_CLIENT_SECRET" config variables set.
        '''
        super().__init__(secerts)

        if ("REDDIT_OAUTH_CLIENT_ID" not in secerts) or ("REDDIT_OAUTH_CLIENT_SECRET" not in secerts) or ("REDDIT_OAUTH_REDIRECT_URI"):
            raise ValueError(secerts)

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
        url = "https://ssl.reddit.com/api/v1/authorize?" + urllib.urlencode(params)
        return url

    def validate_credentials() -> bool:
        '''
        Check if the credentials are correct with Reddit.\n
        Returns dictionary of user information if verification is successful, otherwise the value 'None'.
        '''
        pass
    

class AuthenticatorFactory:

    def __init__(self, option, credentials):
        self.__authenticators = {"REDDIT": RedditAuthenticator}
        if option in self.__authenticators:
            return self.__authenticators[option](credentials)
        else:
            raise ValueError(option)
    
    def get_options(self):
        return self.__authenticators.keys()

    def _authenticate_with_reddit():
        pass
    