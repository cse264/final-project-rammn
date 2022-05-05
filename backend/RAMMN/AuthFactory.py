from ast import Dict
from flask import current_app, g
from RAMMN.ExternalAPIAuthenticator import ExternalAPIAuthenticator
from RAMMN.RedditAuthenticator import RedditAuthenticator

class AuthenticatorFactory:

    def __init__(self):
        '''
        The authenticator Factory creates the following authenticators:\n
        Reddit.
        '''
        self.__authenticators = {"REDDIT": RedditAuthenticator}

    def get_authenticator(self, option: str) -> ExternalAPIAuthenticator:
        '''
        In the request lifetime, the authenticator is created once!\n
        In case the secerts need to be changed after authenticator construction, use ExternalAPIAuthenticator.set_secerts()
        '''
        if option in self.__authenticators:

            if option not in g:
                setattr(g, option, self.__authenticators[option](current_app.config))

            return getattr(g, option)

        else:
            raise ValueError(option)

    def get_options(self):
        return self.__authenticators.keys()
