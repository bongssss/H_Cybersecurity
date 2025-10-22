# import re
# import json
# import csv
# from  bs4 import BeautifulSoup

# # ----------------------
# # Regex Patterns
# # ----------------------
# NAME_REGEX = re.compile(r"^[A-Za-z]+(?:\s[A-Za-z]+)+$")
# EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# PHONE_REGEX = re.compile(r"\+?\d{1,3}?[\s.-]?\(?\d{1,4}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,9}")

# # ----------------------
# # Function to extract data
# # ----------------------
# def extract_pii_from_text(text):
#     names = NAME_REGEX.findall(text)
#     emails = EMAIL_REGEX.findall(text)
#     phones = PHONE_REGEX.findall(text)
#     return emails, phones, names

# # ----------------------
# # Parse JSON File
# # ----------------------
# def parse_json_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     text_content = json.dumps(data)
#     return extract_pii_from_text(text_content)

# # ----------------------
# # Parse HTML File
# # ----------------------
# def parse_html_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         soup = BeautifulSoup(f, "html.parser")

#     text_content = soup.get_text(separator=" ")
#     return extract_pii_from_text(text_content)

# # ----------------------
# # Save to CSV
# # ----------------------
# def save_to_csv(emails, phones, names, output_file="parsed_data.csv"):
#     with open(output_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Email", "Phone", "Name"])

#         max_len = max(len(emails), len(phones), len(names))
#         for i in range(max_len):
#             name = names[i] if  i < len(names) else ""
#             email = emails[i] if i < len(emails) else ""
#             phone = phones[i] if i < len(phones) else ""
#             writer.writerow([name, email, phone])

# # ----------------------
# #  Run
# # ----------------------
# if __name__ == "__main__":
#     # Try with a JSON dump
#     emails, phones, names = parse_json_file("darkweb_mock_prep/messy_data.json")

#     # Or try with HTML scraped content
#     # emails, phones = parse_html_file("messy_data.html")

#     save_to_csv(emails, phones, names)
#     print(f"Extracted {len(names)} names, {len(emails)} emails and {len(phones)} phone numbers.")
import re
import json
import csv
from  bs4 import BeautifulSoup

# ----------------------
# Regex Patterns
# ----------------------
# This pattern now finds text inside quotes following a "name" key.
# The parentheses create a "capturing group," so findall returns only the name itself.
NAME_REGEX = re.compile(r'"name":\s*"([A-Za-z]+(?:\s[A-Za-z]+))"')
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+(?:@|\[at\])[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"[+(]?\d{3}?[)]?[\s.-]?\(?\d{1,4}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,9}")

# ----------------------
# Function to extract data
# ----------------------
def extract_pii_from_text(text):
    names = NAME_REGEX.findall(text)
    emails = EMAIL_REGEX.findall(text)
    phones = PHONE_REGEX.findall(text)
    return emails, phones, names

# ----------------------
# Parse JSON File
# ----------------------
def parse_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # The regex is run on the entire file converted to a string
    text_content = json.dumps(data)
    return extract_pii_from_text(text_content)

# ----------------------
# Parse HTML File
# ----------------------
def parse_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    text_content = soup.get_text(separator=" ")
    return extract_pii_from_text(text_content)

# ----------------------
# Save to CSV
# ----------------------
def save_to_csv(emails, phones, names, output_file="parsed_data.csv"):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Phone"])

        max_len = max(len(emails), len(phones), len(names))
        for i in range(max_len):
            name = names[i] if  i < len(names) else ""
            email = emails[i] if i < len(emails) else ""
            phone = phones[i] if i < len(phones) else ""
            writer.writerow([name, email, phone])

# ----------------------
# Helper to create the mock file
# ----------------------


# ----------------------
#  Run
# ----------------------
if __name__ == "__main__":

        # Try with a JSON dump
    emails, phones, names = parse_json_file("darkweb_mock_prep/messy_data.json")

    # Or try with HTML scraped content
    # emails, phones, names = parse_html_file("messy_data.html")

    save_to_csv(emails, phones, names)
    print(f"Extracted {len(names)} names, {len(emails)} emails and {len(phones)} phone numbers.")