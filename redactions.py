import re

email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
card = r"\d{4}[-\s]\d{1,6}[-\s]\d{1,5}[-\s]\d{1,5}|\d{4}[-\s]\d{6}[-\s]\d{1,5}"
international_phone = r"\+\d{1,2}[-\s]+\d{3}[-\s]+\d{1,3}[-\s]+\d{4}"
phone = r"\(\d{3}\)[-\s]*\d{3}[-\s]*\d{4}|\d{3}[-\s]*\d{3}[-\s]*\d{4}|\d{10}"
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
    "Email": email,
    "Credit Card": card,
    "International Phone": international_phone,
    "Phone":phone,
    "SSN": ssn,
}

redacted_text, count = redact(text, patterns)

with open('output.txt', 'w') as file:
    file.write(redacted_text)

log = "Redaction Summary:\n\n"
redactions = 0

for pattern, count in count.items():
    log += f"{pattern}: {count} redaction(s)\n"
    redactions += count

log += f"\nTotal redactions: {redactions}"

with open('log.txt', 'w') as log_file:
    log_file.write(log)

print("Redaction completed!")
print(f"Total redactions: {redactions}")
