# -*- coding: UTF-8 -*-

from PROIE import *

if __name__ == '__main__':
    #####
    # path_in_img = "resources/palmprint.jpg"
    path_in_img = "resources/sample.tif"

    proie = PROIE()

    # proie.extract_roi(path_in_img, rotate_90_clockwise_times=1)
    proie.extract_roi(path_in_img, rotate_90_clockwise_times=2)

    proie.show_result()

    # proie.save("resources/palmprint_roi.jpg")
    proie.save("resources/sample_roi.tif")
