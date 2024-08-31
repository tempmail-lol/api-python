# TempMail.lol Python API
<a href="https://discord.gg/GHapeHPWVS">
    <img alt="discord" src="https://discord.com/api/guilds/899020130091139082/widget.png">
</a>

This repository is for the [TempMail.lol](https://tempmail.lol/) Python API.

## Updating form v2
The library is **completely** different from version 2.x.x.  Please see Usage to learn more about the changes to the Python library.

Please switch to the new version of the library if you are using a new API key.  If you are still using a BananaCrumbs ID, you must use v2.

## Installation

You can install the TempMail API using PIP:
```
pip install tempmail-lol
```

## TempMail Plus and Ultra

If you have a TempMail Plus or Ultra subscription, you can use it in the API.  Please see the usage below.  If you need help, ask in our Discord server above or email us at contact@bananacrumbs.us.

**You do not need an API key to use the free tier of TempMail**.

## Usage
```python
from TempMail import TempMail

# Create a new TempMail object
tmp = TempMail()

# If you have an API Key, use it here (you do not need an API key to use the free tier)
tmp = TempMail("tm.1234567890.randomcharactershere")

# Generate an inbox with a random domain and prefix
inb = tmp.createInbox()

# Or... use a prefix
inb = tmp.createInbox(prefix = "joe")

# Generate an inbox using a specific domain (you can also use your custom domain here)
# Prefixes on custom domains has no extra characters.  For example, a custom domain example.com
# with a prefix of "whoever" will make "whoever@example.com".  If you do not provide a prefix,
# a random one will be created for you.
inb = tmp.createInbox(domain = "mycustomdomain.com", prefix = "optional")

# Check for emails (throws exception on invalid token)
emails = tmp.getEmails(inb)

# Or... use the token (which is a string)
emails = tmp.getEmails(inb.token)

print("Emails:")

for email in emails:
    print("\tSender: " + email.sender)
    print("\tRecipient: " + email.recipient)
    print("\tSubject: " + email.subject)
    print("\tBody: " + email.body)
    print("\tHTML: " + str(email.html)) # may be None
    print("\tDate: " + str(email.date)) # Unix timestamp in milliseconds
```

## Custom Domain Keys
Note that the token for custom inboxes is stored on your domain as a text record with a name of `_tmpml` and a sha512 hash.

See more details in [accounts.tempmail.lol](https://accounts.tempmail.lol).

