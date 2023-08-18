import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    # Open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input doesn't exist")
    # Open the shirt
    shirtfile = Image.open("shirt.png")

    # Get the size of the shirt
    size = shirtfile.size

    # Resize the muppet image to fit the shirt
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)
    # Create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    # Check if it is an image file
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    # Check if the extension of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extension")

def check_extension(file):
    if file in [".jpg", ".png", ".jpeg"]:
        return True
    return False


if __name__ == "__main__":
    main()

