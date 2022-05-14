class TempMail:

    BASE_URL = "https://api.tempmail.lol";

    
    
    """
     * Make an HTTP request to the TempMail API.
     * 
     * @param endpoint The endpoint to make the request to.
     * @return The response as a {@link String} from the server, or {@code null} if there is no response data.
     * @throws IOException If the request fails.
     *"""
        
    def makeHTTPRequest(endpoint):
        headers = {
            "User-Agent": "TempMailJavaAPI/1.0",
            "Accept": "application/json"
        }
        connection = requestes.get(BASE_URL + endpoint, headers=headers)
        
        #read all the info from the website
        response = connection.text
        
        return response
    