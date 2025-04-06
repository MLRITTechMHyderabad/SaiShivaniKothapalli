import re

text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."
pattern = r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.(?:[a-zA-Z]{2,})(?:\.[a-zA-Z]{2,})?\b'
emails = re.findall(pattern, text)
print(emails)
