# Folosit inception score de la:
# https://github.com/openai/improved-gan

from model import get_inception_score
import os
import cv2

IMAGE_DIR = "/content/BIRDS/My Drive/validation/valid/single"
# "/home/edy/Desktop/Master/Semestrul 2/Research/AttnGAN-Python2/models/bird_AttnGAN2/valid/single/"

def main():
    # print ("suntem in main!!!")

    big_dir = os.listdir(IMAGE_DIR)
    big_dir = sorted(big_dir)
    list_images = []

    print ("IMAGE_DIR is" + IMAGE_DIR)

    index_dir = 0
    for img_category in big_dir:
        dir_path = IMAGE_DIR + "/" + img_category
        # print (dir_path)

        list_img_paths = os.listdir(dir_path)

        cnt = 0
        for img_path in list_img_paths:
            # print (img_path)
            cnt += 1

            crt_path = dir_path + "/" + img_path
            # print (crt_path)
            crt_img = cv2.imread(crt_path)

            # print (type(crt_img))
            list_images.append(crt_img)

        index_dir += 1
        print (str(index_dir) + ". Total of " + str(cnt) + " images at " + img_category)

    # print (list_img_paths)
    print ("We have a total of: " + str(len(list_images)) + " images!")
    nr_splits = 10
    results = get_inception_score(list_images, splits=nr_splits)

    print ("Results are:", results)
    print ("Nr_splits were: " + str(nr_splits))

if __name__ == "__main__":
    main()