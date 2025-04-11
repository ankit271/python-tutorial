import re

# Sample text
text = """
Hello, you can reach out 8202325252 to us at support@example.com or sales@example.org.
For personal inquiries, contact john.doe123@example.net or jane_doe@example.co.uk.
Mobile No-8286787925                    
"""

# Regular expression pattern for mobile number
mobile_pattern = r'(\d{10})'

# Find mobile number
mobile = re.findall(mobile_pattern, text)

for i in mobile:
    print(i)
