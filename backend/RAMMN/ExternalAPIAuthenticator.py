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