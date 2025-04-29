url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")