import re

# find and replace Regex
# re.sub(pattern, repl, string, count=0, flags=0)

url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.com)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.com)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))

