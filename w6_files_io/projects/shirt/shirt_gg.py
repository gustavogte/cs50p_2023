import sys
import os
from PIL import Image, ImageOps

def main():
    check_file()
    input_file, output_file = check_file()
    put_shirt(input_file, output_file)

def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (
        sys.argv[1].strip().lower().endswith(".jpg") == False
        and sys.argv[2].strip().lower().endswith(".jpg") == False
        and sys.argv[1].strip().lower().endswith(".jpeg") == False
        and sys.argv[2].strip().lower().endswith(".jpeg") == False
        and sys.argv[1].strip().lower().endswith(".png") == False
        and sys.argv[2].strip().lower().endswith(".png") == False
    ):
        sys.exit("Invalid input")
    elif( len(sys.argv[1].split(".")) < 2 or len(sys.argv[2].split(".")) < 2
    ):
        sys.exit("Invalid input")
    else:
        input_file = sys.argv[1].split(".")
        output_file = sys.argv[2].split(".")
        if input_file[1] != output_file[1]:
            sys.exit("Input and output have different extensions")
        else:
            input_file = sys.argv[1]
            output_file = sys.argv[2]
            return input_file, output_file

def put_shirt(input_file, output_file):

    """
    Image.paste(im, box=None, mask=None)[source]
    Pastes another image into this image. The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, right, and lower pixel coordinate, or None (same as (0, 0)). See Coordinate System. If a 4-tuple is given, the size of the pasted image must match the size of the region.
    If the modes don’t match, the pasted image is converted to the mode of this image (see the convert() method for details).
    """
    #try:
    input_image = Image.open(input_file)
    #print(input_image)
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    print(shirt_size)
    print(output_file)
    new_output_image = ImageOps.fit(input_image, shirt_size)

    output_image = new_output_image.paste(new_output_image, mask=shirt)
    output_image.save(output_file)

    print(output_image)
    #output_file.save(output_image)

    #except(FileNotFoundError):
    #sys.exit("Input does not exist")



if __name__ == "__main__":
    main()
