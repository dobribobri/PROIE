# -*- coding: UTF-8 -*-

from PROIE import *


def example_1():
    path_in_img = "resources/palmprint.jpg"

    proie = PROIE()

    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=1)

    proie.show_result()

    proie.save("resources/palmprint_roi.jpg")


def example_2():
    path_in_img = "resources/sample.tif"

    proie = PROIE()

    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL)

    proie.show_result()

    proie.save("resources/sample_roi.tif")


if __name__ == '__main__':
    example_1()
    example_2()
