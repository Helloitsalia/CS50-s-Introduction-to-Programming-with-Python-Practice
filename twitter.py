import re 

url = input("URL:").strip()

matches = re.search(r"^http?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))