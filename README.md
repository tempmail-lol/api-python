# TempMail.lol Python API
![image](https://img.shields.io/badge/Active-YES-brightgreen)

This repository is for the [TempMail.lol](https://tempmail.lol/) Python API.

## Installation

Use this commands to install dependency.
```
pip install requests
```
Place the directory `TempMail` into your root directory where your main python file is located. 

EX:

![image](https://user-images.githubusercontent.com/32007930/168915320-963ffe0e-3b00-45ca-91f1-6f72aa99d8ee.png)

## Usage
```python
from TempMail.TempMail import * #imports everything from TempMail library
import time #import time module

inbox = TempMail.generateInbox() #returns an Inbox object with Email and Token

print("Email Address: "+ inbox.address) #View output below
print("Authorization Token: "+ inbox.token)

#output: 
"""
    Email Address: m8h69n52824315@theeyeoftruth.com
    Authorization Token: RCfc1og1z1JzuN1mkXL2eFdAc_8uxSRAwcGhUoXuH26e7nnJMdVVtSxxasZLD9D2OHTKIjVEvLhK7S0K5QIanA
"""

while(True): #Infinite Loop
    emails = TempMail.getEmails(inbox) #Returns list of Email objects
    print(emails) # View output below
    time.sleep(30) #wait 30 sec

#output:
"""
    [Email (sender=ExampleEmail@gmail.com, recipient=d6inmp52824914@magicaljellyfish.com, 
            subject=Subject line, body=Text Area, html=<div dir="ltr">Text Area</div>, 
            date=1652824961713 )]
"""
```
