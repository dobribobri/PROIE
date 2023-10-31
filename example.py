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
    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL_LEFT)
    proie.show_result()
    proie.save("resources/sample_roi.tif")


def example_3():
    # path_in_img = "resources/person_004_db1_R2.tif"   # raises error
    path_in_img = "resources/person_002_db1_R3.tif"
    proie = PROIE()
    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL_RIGHT)
    proie.show_result()


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
