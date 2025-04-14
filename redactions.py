import re

email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
card = r"\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}|\d{4}[-\s]\d{6}[-\s]\d{5}"
international = r"\+\d{1,2}\s\d{3}\s\d{1,3}\s\d{4}"
phone = r"\(\d{3}\)[-\s]*\d{3}[-\s]*\d{4}|\d{3}[-\s]*\d{3}[-\s]*\d{4}"
ssn = r"\b\d{3}-\d{2}-\d{4}\b"

def redact(text, patterns):
    count = {}
    
    for pattern, regex in patterns.items():
        matches = re.findall(regex, text)
        count[pattern] = len(matches)
        text = re.sub(regex, "[REDACTED]", text)   
    return text, count

with open('input.txt', 'r') as file:
    text = file.read()

patterns = {
    "Email id": email,
    "Credit Card Number": card,
    "International Phone Number": international,
    "Domestic Phone Number":phone,
    "SSN": ssn,
}

redacted_text, count = redact(text, patterns)

with open('output.txt', 'w') as file:
    file.write(redacted_text)

log = "Logs summarized:\n\n"
redactions = 0

for pattern, count in count.items():
    log += f"No.of {pattern}'s redacted : {count}\n"
    redactions += count

log += f"\nTotal count of redacted data: {redactions}"

with open('log.txt', 'w') as log_file:
    log_file.write(log)

print("Redaction of data completed!")
print(f"Total redactions: {redactions}")
