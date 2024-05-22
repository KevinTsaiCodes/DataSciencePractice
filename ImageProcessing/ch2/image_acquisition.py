import argparse
import cv2

def parse_args():
    parser = argparse.ArgumentParser(description="A CLI tool for reading, showing and writing the image.")
    parser.add_argument("-i", "--input_image", description="path/to/the/input/image/file", default="figs/lena.jpg")
    return parser.parse_args()


def read_image(filename):
    file = cv2.imread(filename)
    is_exist = file
    if is_exist == 'None':
        print(f"{filename} not found")
        exit(1)


def main(opt):
    pass



if __name__ == '__main__':
    opt = parse_args()
    main(opt)