## Submission for Kisan Quest
https://devpost.com/


## Inspiration
Inspiration to build this project was the need to secure the sensitive data.
I wanted to create a simple tool to safeguard the sensitive data.
## What it does
**SilentSeal** is a Python-based tool that scans text files for following sensitive information:
- Email address
- Phone numbers
- Credit card numbers
- Social Security Numbers (SSNs)

It replaces all detected sensitive information with `[REDACTED]` and saves the cleaned version to a new file. 
A log file summarizes the number of redactions for each type of sensitive data.

## How I built it
I built **SilentSeal** using Python and its powerful `re` module for regular expressions. The steps included are:
1. Designing regex patterns to detect various types of sensitive data.
2. Writing a function to scan text files, replace sensitive content with `[REDACTED]`, and count the number of redactions.
3. Implementing file handling to read input files, write redacted output files, and generate a log file.
4. Testing the tool with various input formats to ensure accuracy and correctness.

## Challenges I ran into
- **Regex Complexity**: Crafting regex patterns that accurately detect sensitive data while avoiding false positives was challenging. 
- **Handling Edge Cases**: Ensuring the tool works with different text formats, such as multiline inputs, mixed content, and international phone numbers, ssn required extensive testing and debugging.

## Accomplishments that I am proud of
- Designing regex patterns that guarantees precision and flexibility.
- Successfully creating a tool that accurately detects and redacts multiple types of sensitive data.
- Building a user-friendly solution that generates both redacted output and a detailed log file.
- Ensuring the tool is robust and handles edge cases effectively.

## What I learned
- The power of Python's `re` module for pattern matching.
- How to design efficient and accurate regex patterns.
- The importance of testing and debugging to handle edge cases and ensure reliability.

## What's next for SilentSeal
- **Enhanced Detection**: Add support for detecting additional sensitive data types, such as IP addresses and bank account numbers.
- **GUI Integration**: Build a graphical user interface (GUI) to make the tool more accessible to non-technical users.
- **Real-Time Redaction**: Extend the tool to redact sensitive data in real-time from live streams or logs.
- **Cloud Integration**: Enable cloud-based processing for large-scale data redaction.
