import requests
import json
from TempMail.Email import Email
from TempMail.Inbox import Inbox

class TempMail:
    global BASE_URL
    BASE_URL = "https://api.tempmail.lol"
    
    
    """
    Make a request to the tempmail.lol api with a given endpoint
    The content of the request is a json string and is returned as a string object
    """
        
    def makeHTTPRequest(endpoint):
        headers = {
            "User-Agent": "TempMailPythonAPI/1.0",
            "Accept": "application/json"
        }
        try:
            connection = requests.get(BASE_URL + endpoint, headers=headers)
            if connection.status_code >= 400:
                raise Exception("HTTP Error: " + str(connection.status_code))
        except Exception as e:
            print(e)
            return None

        response = connection.text
        
        return response

    """
    GenerateInbox will generate an inbox with an address and a token
    and returns an Inbox object
    """
    def generateInbox(rush = False):
        try :
            s = TempMail.makeHTTPRequest("/generate" + ("/rush" if rush else ""))
        except:
            print("Website responded with: "+ s)
        data = json.loads(s)
        return Inbox(data["address"], data["token"])
        

    """
    getEmail gets the emails from an inbox object
    and returns a list of Email objects
    """
    def getEmails(inbox):
        s = TempMail.makeHTTPRequest("/auth/" + inbox.token)
        data = json.loads(s)

        #Raise an exception if the token is invalid
        if "token" in s:
            if data["token"] == "invalid":
                raise Exception("Invalid Token")

        #if no emails are found, return an empty list
        #else return a list of email
        if data["email"] == None:
            return ["None"]
        else:
            emails = []
            for email in data["email"]:
                emails.append(Email(email["from"], email["to"], email["subject"], email["body"], email["html"], email["date"]))
            return emails
        