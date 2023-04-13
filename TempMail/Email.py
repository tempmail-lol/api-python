"""
Email class is used to store the email data which consists of
the sender, recipient, subject, body, html and date
"""

class Email:
    def __init__(self, sender, recipient, subject, body, html, date):
        #make the propertys immutable using @property
        self._sender = sender
        self._recipient = recipient
        self._subject = subject
        self._body = body
        self._html = html
        self._date = date
    
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
    def html(self):
        return self._html
    
    @property
    def date(self):
        return self._date
    
    def __repr__(self):
        return ("Email (sender={}, recipient={}, subject={}, body={}, html={}, date={} )"
                .format(self.sender, self.recipient, self.subject, self.body, self.html, self.date))