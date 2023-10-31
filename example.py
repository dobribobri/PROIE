# -*- coding: UTF-8 -*-
import os
from PROIE import *


def example(path: str, n: int, mode: Mode):
    proie = PROIE()
    proie.extract_roi(path, rotate_90_clockwise_n_times=n, mode=mode)
    proie.show_result()


def example_2():
    path_in_img = "resources/sample.tif"
    proie = PROIE()
    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL_LEFT)
    proie.show_result()
    proie.save("resources/sample_roi.tif")


def example_3():
    path_in_img = "resources/person_002_db1_R3.tif"
    proie = PROIE()
    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL_RIGHT)
    proie.show_result()


def example_4():
    path_in_img = "resources/person_004_db1_R2.tif"   # raises error
    proie = PROIE()
    proie.extract_roi(path_in_img, rotate_90_clockwise_n_times=2, mode=Mode.DORSAL_RIGHT)
    proie.show_result()


if __name__ == '__main__':
    example(path=os.path.join("resources", "palmprint.jpg"), n=1, mode=Mode.VENTRAL)
    example(path=os.path.join("resources", "sample.tif"), n=2, mode=Mode.VENTRAL)
    example(path=os.path.join("resources", "person_002_db1_R3.tif"), n=2, mode=Mode.VENTRAL)
    example(path=os.path.join("resources", "person_004_db1_R2.tif"), n=2, mode=Mode.VENTRAL)
