import re

tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"
pattern = r'#\w+'
hashtags = re.findall(pattern, tweet)
print(hashtags)
