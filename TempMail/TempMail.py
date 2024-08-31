import requests
import json
from TempMail.Email import Email
from TempMail.Inbox import Inbox

class TempMail:
    global BASE_URL
    BASE_URL = "https://api.tempmail.lol/v2"
    
    # constructor
    def __init__(self, api_key = None):
        self.api_key = api_key

    def makeHTTPRequest(self, endpoint, method = "GET", data = None):
        headers = {
            "User-Agent": "TempMailPythonAPI/3.0",
            "Accept": "application/json"
        }
        
        if self.api_key is not None:
            headers["Authorization"] = "Bearer " + self.api_key
        
        if method == "POST":
            headers["Content-Type"] = "application/json"
            connection = requests.post(BASE_URL + endpoint, headers = headers, data = data)
        else:
            connection = requests.get(BASE_URL + endpoint, headers = headers)
        
        # Check some error codes
        # This includes rate limits, auth errors, and server errors
        if connection.status_code == 429:  # Rate limit
            raise Exception("TempMail Rate Limit: " + connection.text)
        elif 400 <= connection.status_code < 500:  # Client error
            raise Exception("HTTP Error: " + str(connection.status_code) + " " + connection.text)
        elif 500 <= connection.status_code < 600:  # Server error
            raise Exception("TempMail Server returned an error: " + str(connection.status_code) + " " + connection.text + " please report this.")
        
        response = connection.text
        
        return response

    """
    Creates an inbox with an address and a token.  Returns an Inbox object.
    
    You can also specify your custom domain if you are logged in with an API key (it must be the same API key which made the domain record).
    
    > domain = None will generate an inbox with a random domain
    > prefix = None will generate an inbox with a random prefix
    """
    def createInbox(self, domain = None, prefix = None):
        url = "/inbox/create"
        
        payload = json.dumps({"domain": domain, "prefix": prefix})
        
        s = TempMail.makeHTTPRequest(self, url, "POST", payload)
        
        data = json.loads(s)
        
        return Inbox(data["address"], data["token"])
    
    """
    Get the inbox by its token.  Returns an array of Email objects.
    
    Will throw an exception if the token is invalid or expired.
    
    > inbox Required
    """
    def getEmails(self, inbox):
        # if inbox is an instance of Inbox object, get the token, otherwise inbox is a string
        if isinstance(inbox, Inbox):
            token = inbox.token
        else:
            token = inbox

        s = TempMail.makeHTTPRequest(self, "/inbox?token=" + token)
        data = json.loads(s)
        
        if data["expired"] is True:
            raise Exception("Token Expired")
        
        # if no emails are found, return an empty list
        # else return a list of email
        if data["emails"] is None:
            return []
        else:
            emails = []
            for email in data["emails"]:
                # Some emails may not have html, so we will check for that
                if "html" in email:
                    emails.append(
                        Email(email["from"], email["to"], email["subject"], email["body"], email["html"], email["date"]))
                else:
                    emails.append(
                        Email(email["from"], email["to"], email["subject"], email["body"], None, email["date"]))
            return emails
    
    """
    Legacy custom domain checking.  Please only use this if you need to, as this method is not good compared to creating individual inboxes on your domain.
    > domain Required
    """
    def checkCustomInboxLegacy(self, domain):
        url = "/custom?domain=" + domain
        
        s = TempMail.makeHTTPRequest(self, url)
        data = json.loads(s)
        
        # There is no way to check if the token is invalid
        # so we will just return an empty list if there are no emails
        if data["email"] is None:
            return []
        else:
            emails = []
            for email in data["email"]:
                emails.append(
                    Email(email["from"], email["to"], email["subject"], email["body"], email["html"], email["date"]))
            return emails
