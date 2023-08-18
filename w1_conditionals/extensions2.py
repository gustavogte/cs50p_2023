def main():
    file = input("File name: ")
    print(f_type(file))

def f_type(f):
    f = f.strip().lower()
    if f.endswith(".gif"):
        return "image/gif"
    elif f.endswith(".jpeg") or f.endswith(".jpg") :
        return "image/jpeg"
    elif f.endswith(".png"):
        return "image/png"
    elif f.endswith(".pdf"):
        return "application/pdf"
    elif f.endswith(".txt"):
        return "text/plain"
    elif f.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()