class Email:
    def __init__(self, sender, recipient, subject, body, html, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.html = html
        self.date = date