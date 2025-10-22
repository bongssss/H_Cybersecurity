import json

# Create a messy JSON dataset with mixed structured/unstructured data
messy_data = {
    "users": [
        {
            "id": 1,
            "name": "Alice Example",
            "contact": "alice.example123@gmail.com, +1-202-555-0147",
            "notes": "Interested in security research, joined 2022."
        },
        {
            "id": 2,
            "name": "Bob Test",
            "contact": "bobtest[at]mail.com / phone: (202) 555-0173",
            "notes": "Old record, not verified."
        },
        {
            "id": 3,
            "name": "Charlie Hacker",
            "contact": "Email: charlie_h@protonmail.com, mobile: +44 7700 900123",
            "notes": "Suspicious activity on forums."
        }
    ],
    "raw_dump": """
        Random forum post: Reach me at johnny77@yahoo.com 
        or call me at 202.555.0199 ASAP!!
        Another one: support@darkmarket.onion - hidden contact
    """,
    "metadata": {
        "source": "darkweb_forum_scrape",
        "timestamp": "2025-09-30T10:00:00Z"
    }
}

# Save as messy_data.json
file_path = "darkweb_mock_prep/messy.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(messy_data, f, indent=4)

file_path
