def main():
    file = input("File name: ")
    print(f_type(file))

def f_type(f):
    f = f.strip().lower()
    match f:
        case f.endswith(".gif"):
            return "image/gif"
        case f.endswith(".jpeg") | f.endswith(".jpg"):
            return "image/jpeg"
        case f.endswith(".png"):
            return "image/png"
        case f.endswith(".pdf"):
            return "application/pdf"
        case f.endswith(".txt"):
            return "text/plain"
        case f.endswith(".zip"):
            return "application/zip"
        case _:
            return "application/octet-stream"

main()