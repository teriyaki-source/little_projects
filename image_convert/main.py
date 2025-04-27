from PIL import Image
import os

def iterate_file(in_directory, out_directory, scale):
    for file in os.listdir(os.fsencode(in_directory)):
        filename = os.fsdecode(file)
        head,sep,tail = filename.partition(".")
        if filename.endswith(".jpeg"):
            ascii_conversion(in_directory + filename, out_directory + head, scale, out_directory)

def ascii_conversion(file, target, scale, out_directory):
    img = Image.open(file)
    w, h = img.size

    if scale != 1:
        img.resize((w//scale, h//scale)).save(out_directory + "resized.jpeg")
        img = Image.open(out_directory + "resized.jpeg")
        w,h = img.size

    chars = []
    for i in range(h):
        chars.append(["X"]*w)
    
    pixels = img.load()

    for y in range(h):
        for x in range(w):
            tot = sum(pixels[x,y])
            if tot in range(1,25):
                chars[y][x] = "@"
            elif tot in range(25,100):
                chars[y][x] = "#"
            elif tot in range(100,200):
                chars[y][x] = "*"
            elif tot in range(200,300):
                chars[y][x] = "0"
            elif tot in range(300,400):
                chars[y][x] = "/"
            elif tot in range(400,500):
                chars[y][x] = ":"
            elif tot in range(500,600):
                chars[y][x] = "\""
            elif tot in range(600,700):
                chars[y][x] = "'"
            elif tot in range(700, 765):
                chars[y][x] = "."
            else:
                chars[y][x] = " "
    out = open("%s.txt" % target, "a")

    for row in chars:
        out.write("".join(row) + "\n")
    out.close()

    if os.path.exists(out_directory + "resized.jpeg"):
        os.remove(out_directory + "resized.jpeg")

def main():
    # insert .jpeg images into the named directory and it will convert them into scaled
    # text equivalent images of the same name, saved in the output folder
    # scale will scale the images down by the set amount
    in_directory = "./images/"
    out_directory = "./output/"
    scale = 4
    iterate_file(in_directory, out_directory, scale)

if __name__ == "__main__":
    main()