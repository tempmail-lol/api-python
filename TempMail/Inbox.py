"""
The class Inbox stores an address and an authorization token
"""

class Inbox:
    def __init__(self, address, token):
        #make the propertys immutable using @property
        self._address = address
        self._token = token

    @property
    def address(self):
        return self._address

    @property
    def token(self):
        return self._token
    
    def __repr__(self):
        return ("Inbox (address={}, token={} )"
                .format(self.address, self.token))