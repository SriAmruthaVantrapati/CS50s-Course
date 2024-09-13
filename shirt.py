import sys
from PIL import Image, ImageOps


def main():
    file_open(sys.argv)

    main_img = sys.argv[1]
    output_img = sys.argv[2]

    # get size of overlay shirt
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size

    # open main_img
    img_1 = Image.open(main_img)
    # crop the main_img to the shirt_size
    cropped_main_img = ImageOps.fit(img_1, shirt_size)

    # paste the shirt onto the cropped main_img
    cropped_main_img.paste(shirt, shirt)

    # save the image with the shirt overlay
    cropped_main_img.save(output_img)


def is_image_file(filename):
    return filename.strip().lower().endswith((".jpg", ".jpeg", ".png"))


def get_extension(filename):
    return filename.strip().lower().split(".")[-1]


def file_open(v):
    if len(v) < 3:
        sys.exit("Too few command-line arguments")
    if len(v) > 3:
        sys.exit("Too many command-line arguments")
    if not (is_image_file(v[1]) and is_image_file(v[2])):
        sys.exit("Invalid input")
    if get_extension(v[1]) != get_extension(v[2]):
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
