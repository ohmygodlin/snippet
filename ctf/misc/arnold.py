#boom, meituan-2021, https://mp.weixin.qq.com/s/l1xejiNFzzefi_5NUJsQ7g

import numpy as np
import matplotlib.pyplot
from skimage.io import imread, imshow
import time
import math
import cv2

def arnold_decode(image, shuffle_times, a, b):
    decode_image = np.zeros(shape=image.shape)
    h, w = image.shape[0], image.shape[1]
    N = h
    for time in range(shuffle_times):
        for ori_x in range(h):
            for ori_y in range(w):
                new_x = ((a*b+1)*ori_x + (-b)* ori_y)% N
                new_y = ((-a)*ori_x + ori_y) % N
                decode_image[new_x, new_y] = image[ori_x, ori_y]
    cv2.imshow("image",decode_image)
    cv2.waitKey(10)
    cv2.imwrite(i,decode_image)
    return decode_image

final = imread('flag.png')

for z in range(0,100):
    i = str(z) + '.png'
    arnold_decode(final, 10, z,z)