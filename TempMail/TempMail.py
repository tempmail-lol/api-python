import requests
import json
from Email import Email
from Inbox import Inbox

class TempMail:
    global BASE_URL
    BASE_URL = "https://api.tempmail.lol"
    
    
    """
     * Make an HTTP request to the TempMail API.
     * 
     * @param endpoint The endpoint to make the request to.
     * @return The response as a {@link String} from the server, or {@code null} if there is no response data.
     * @throws IOException If the request fails.
     *"""
        
    def makeHTTPRequest(endpoint):
        headers = {
            "User-Agent": "TempMailPythonAPI/1.0",
            "Accept": "application/json"
        }
        connection = requests.get(BASE_URL + endpoint, headers=headers)
        
        #read all the info from the website
        response = connection.text
        
        return response

    """
    Generate a new {@link Inbox}.
    
    @return The new {@link Inbox}, or {@code null} if the request fails.
    """
    def generateInbox():
        try :
            s = TempMail.makeHTTPRequest("/generate")
        except:
            print("Website responded with: "+ s)
        data = json.loads(s)
        return Inbox(data["address"], data["token"])
        

    """
    Get emails from the inbox provided the {@link Inbox}.
    @param inbox The inbox to get emails from.
    @return {@link Email[]} The emails received, or {@code null} if there are no emails.
    @raises TempMailTokenExpiredException If the token is invalid.
    """
    def getEmails(inbox):
        try:
            s = TempMail.makeHTTPRequest("/auth/" + inbox.token)
        except:
            print("Website responded with: "+ s)
        data = json.load(s)
        emails = []
        for email in data:
            emails.append(Email(email["from"], email["to"], email["subject"], email["body"], email["html"], email["date"]))
        return emails
        