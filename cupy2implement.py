import cupy
import numpy as np


if __name__ == '__main__':
    np_symbols = dir(np)
    cupy_symbols = dir(cupy)
    for sym in np_symbols:
        if sym in cupy_symbols:
            continue
        if sym.startswith("_"):
            continue
        if sym[0].isupper():
            continue

        print(sym)
