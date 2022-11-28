# TempMail.lol Python API
<a href="https://discord.gg/GHapeHPWVS">
    <img alt="discord" src="https://discord.com/api/guilds/899020130091139082/widget.png">
</a>

This repository is for the [TempMail.lol](https://tempmail.lol/) Python API.

## Installation

Use this command in terminal.
```
pip install tempmail-lol
```

## Usage
```python
from TempMail import TempMail #imports everything from TempMail library
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
