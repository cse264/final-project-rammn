class StructuredResponse(object):
    def __init__(self, status, message=None, data=None):
        self.status = status
        self.message = message
        self.data = data