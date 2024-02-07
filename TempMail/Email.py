"""
Email class is used to store the email data which consists of
the sender, recipient, subject, body, html and date
"""

class Email:
    def __init__(self, sender, recipient, subject, body, date, ip, html):
        #make the propertys immutable using @property
        self._sender = sender
        self._recipient = recipient
        self._subject = subject
        self._body = body
        self._date = date
        self._ip = ip
        self._html = html
        
    
    @property
    def sender(self):
        return self._sender
    
    @property
    def recipient(self):
        return self._recipient
    
    @property
    def subject(self):
        return self._subject
    
    @property
    def body(self):
        return self._body
    
    @property
    def date(self):
        return self._date

    @property
    def ip(self):
        return self._ip
    
    @property
    def html(self):
        return self._html
    
    
    
    def __repr__(self):
        return ("Email (sender={}, recipient={}, subject={}, body={}, date={}, ip={}, html={})"
                .format(self.sender, self.recipient, self.subject, self.body, self.date, self.ip, self.html))