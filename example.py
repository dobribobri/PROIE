# -*- coding: UTF-8 -*-
import os
import re
from PROIE import *


def example(path: str, n: int, mode: Mode):
    proie = PROIE()
    proie.extract_roi(path, rotate_90_clockwise_n_times=n, mode=mode)
    proie.show_result()
    proie.save(path[:-4] + '_roi' + path[-4:])


if __name__ == '__main__':
    example(path=os.path.join("resources", "palmprint.jpg"), n=1, mode=Mode.VENTRAL)
    example(path=os.path.join("resources", "sample.tif"), n=2, mode=Mode.DORSAL)
    example(path=os.path.join("resources", "person_002_db1_R3.tif"), n=2, mode=Mode.DORSAL)
    example(path=os.path.join("resources", "person_004_db1_R2.tif"), n=2, mode=Mode.DORSAL)
