import re

text = """
This is a sample text with some email addresses like info@example.com and 
test@example.org.
It also includes some phone numbers like +1234567890 and +966555123456.
There are also some dates like 2000-01-01, 1999-12-31, and 2023-04-15.
The text also mentions some URLs like https://www.example.com and 
http://www.example.org.
This text is for testing the regular expressions in Python.
It includes various elements like email addresses, phone numbers, dates, and URLs.
This is another sentence with example.com.
"""

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Emails:", emails)

phone_numbers = re.findall(r'\+?\d{11,12}', text)
print("Phone Numbers:", phone_numbers)

dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
print("Dates:", dates)

urls = re.findall(r'http[s]?://[^\s]+', text)
print("URLs:", urls)

sentences = re.findall(r'\b[A-Z][^\.]*\bexample\.com\b[^\.]*\.', text)
print("Sentences with 'example.com':", sentences)
