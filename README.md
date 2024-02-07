# TempMail.lol Python API
<a href="https://discord.gg/GHapeHPWVS">
    <img alt="discord" src="https://discord.com/api/guilds/899020130091139082/widget.png">
</a>

# ----------------------------------------------------
## API v2 update checklist
- [x] **Types**
  - [x] Email
  - [x] Inbox
- [ ] **TempMail Plus/Ultra**
  - [ ] BananaCrumbs ID Authorization
- [ ] **Inbox Methods**
  - [x] Create new inbox
  - [ ] Get emails in an inbox
- [ ] **Custom Domains**
  - [ ] Get emails on a custom domain
  - [ ] Set custom domain ownership
- [ ] **Webhooks**
  - [ ] Set account webhook
  - [ ] Delete account webhook
  - [ ] Set Custom Domain Webhook
- [ ] **Miscellaneous**
  - [ ] Server Stats
  - [ ] Add community domain


# ----------------------------------------------------

This repository is for the [TempMail.lol](https://tempmail.lol/) Python API.

## Updating form v1
The library is different from version 1.x.x.  Please see Usage to learn more about the changes to
the Python library.

## Installation

You can install the TempMail API using PIP:
```
pip install tempmail-lol
```

## TempMail Plus (optional)

Optionally, you can purchase time on a BananaCrumbs ID to get TempMail Plus.  This includes higher rate limits, as well
as some other features.  For more info, see this page: https://tempmail.lol/pricing.html

## Usage
```python
from TempMail import TempMail

# Create a new TempMail object
tmp = TempMail()

# If you have a BananaCrumbs ID, you can login using the constructor
tmp = TempMail("24 number ID", "32 or 36 character token")

# Generate an inbox
inb = TempMail.generateInbox(tmp)

# Generate an inbox using Community (formerly Rush) domains
inb = TempMail.generateInbox(tmp, rush=True)

# Generate an inbox using a specific normal/community domain
inb = TempMail.generateInbox(tmp, rush=False, domain="cringemonster.com")

# Check for emails
emails = TempMail.getEmails(tmp, inbox=inb)

# Check custom domains (requires TempMail Plus)
custom_domain_emails = TempMail.checkCustomInbox(tmp, "example.com", "token given on website")
```

## Custom Domain Keys
Note that the token for custom inboxes is stored on your domain as a text record with a name of `_tmpml` and a sha512 hash.
The token that you submit is the text pre-sha512.  This helps disconnect a user's BananaCrumbs ID and the domain he/she owns.

