import inspect

import cupy
import numpy as np


if __name__ == '__main__':
    np_symbols = dict(inspect.getmembers(np))
    cupy_symbols = dict(inspect.getmembers(cupy))
    functions = []
    modules = []
    others = []
    for sym in np_symbols:
        if sym in cupy_symbols:
            continue
        if sym.startswith("_"):
            continue
        if sym[0].isupper():
            continue

        if inspect.ismodule(np_symbols[sym]):
            modules.append(sym)
        elif inspect.isfunction(np_symbols[sym]):
            functions.append(sym)
        else:
            others.append(sym)

    print("others: ", others)
    print("-"*70)
    print("modules: ", modules)
    print("-"*70)
    print("functions ", functions)
