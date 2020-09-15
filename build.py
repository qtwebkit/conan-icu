#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import platform
import os
import shutil

from bincrafters import build_template_default

if __name__ == "__main__":

    os.system("git submodule update --init conan-center-index")
    subdir = "conan-center-index/recipes/icu/all"
    for f in os.listdir(subdir):
        shutil.move(os.path.join(subdir, f), f)

    builder = build_template_default.get_builder(pure_c=True)

    items = []
    for item in builder.items:
        if item.options["icu:shared"] == True:
            items.append(item)
    builder.items = items

    builder.run()
