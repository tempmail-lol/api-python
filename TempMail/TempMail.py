import requests
import json
from TempMail.Email import Email
from TempMail.Inbox import Inbox


class TempMail:
    global BASE_URL
    BASE_URL = "https://api.tempmail.lol/v2"

    # class vars
    auth_id = None
    auth_token = None

    # constructor
    def __init__(self, auth_id=None, auth_token=None):
        TempMail.auth_id = auth_id
        TempMail.auth_token = auth_token

    """
    Make a request to the tempmail.lol api with a given endpoint
    The content of the request is a json string and is returned as a string object
    """

    def makeHTTPRequest(self, endpoint, requestType, requestData):
        headers = {
            "User-Agent": "TempMailPythonAPI/1.0",
            "Accept": "application/json"
        }

        if TempMail.auth_id is not None and TempMail.auth_token is not None:
            headers["X-BananaCrumbs-ID"] = TempMail.auth_id
            headers["X-BananaCrumbs-MFA"] = TempMail.auth_token

        connection = requests.get(BASE_URL + endpoint, headers=headers)

        # Check some error codes
        # This includes rate limits, auth errors, and server errors
        if connection.status_code == 429:  # Rate limit
            raise Exception("TempMail Rate Limit: " + connection.text)
        elif connection.status_code == 402:  # No time left on account
            raise Exception("BananaCrumbs ID has no time left.  See https://tempmail.lol/pricing.html for more info")
        elif 400 <= connection.status_code < 500:  # Client error
            raise Exception("HTTP Error: " + str(connection.status_code))
        elif 500 <= connection.status_code < 600:  # Server error
            raise Exception("TempMail Server returned an error: " + str(
                connection.status_code) + " " + connection.text + " please report this.")

        response = connection.text

        return response

    """
    GenerateInbox will generate an inbox with an address and a token
    and returns an Inbox object
    application/json options
    ?domain 	string 	Specific domain to use to create an inbox
    ?community 	boolean 	Create a random inbox with a community domain
    ?prefix 	string 	Prefix of the created inbox, otherwise random letters
    """

    def generateInbox(self, inboxType='community', domainString=None, prefixString=None):
        url = "/inbox/create"
        requestType = "POST"
        jsonDataRaw = {}

        match inboxType:
            case 'domain':
                #application/json {domain}
                jsonDataRaw = {
                    "domain": domainString
                }
                break
            case 'community':
                #application/json {community}
                jsonDataRaw = {
                    "community": True 
                }
                break
            case 'prefix':
                #application/json {prefix}
                jsonDataRaw = {
                    "prefix": prefixString 
                }
                break
        
        jsonData = json.dumps(jsonDataRaw)

        s = TempMail.makeHTTPRequest(self, url, requestType, jsonData)
        
        data = json.loads(s)
        return Inbox(data["address"], data["token"])

    """
    getEmail gets the emails from an inbox object
    and returns a list of Email objects
    """

    def getEmails(self, inbox):
        # if inbox is an instance of Inbox object, get the token, otherwise inbox is a string
        if isinstance(inbox, Inbox):
            token = inbox.token
        else:
            token = inbox

        s = TempMail.makeHTTPRequest(self, "/auth/" + token)
        data = json.loads(s)

        # Raise an exception if the token is invalid
        if "token" in s and "token" in data:
            if data["token"] == "invalid":
                raise Exception("Invalid Token")

        # if no emails are found, return an empty list
        # else return a list of email
        if data["email"] is None:
            return ["None"]
        else:
            emails = []
            for email in data["email"]:
                # Some emails may not have html, so we will check for that
                if "html" in email:
                    emails.append(
                        Email(email["from"], email["to"], email["subject"], email["body"], email["html"], email["date"]))
                else:
                    emails.append(
                        Email(email["from"], email["to"], email["subject"], email["body"], None, email["date"]))
            return emails

    """
    checkCustomInbox checks if there are any emails in a custom inbox
    and returns a list of Email objects
    > domain Required
    > token Required
    """
    def checkCustomInbox(self, domain, token):
        url = "/custom/" + token + "/" + domain

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
