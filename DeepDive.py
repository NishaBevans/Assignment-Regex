#Task 1: Email Extraction Enhancement
#Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains.
#(e.g., '[exclude.com][http://exclude.com]) Modify the script to extract all email addresses except those from the specified domain.

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

exclude_domain = "exclude.com"

filtered_emails = [email for email in emails if email.split('@')[1] != exclude_domain]

print(filtered_emails)