#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from bincrafters import (build_template_default,
                         build_template_installer,
                         build_shared)

if __name__ == "__main__":

    if "ARCH" in os.environ:
        arch = os.environ["ARCH"]
        builder = build_template_installer.get_builder()
        builder.add({"os": build_shared.get_os(),
                     "arch_build": arch,
                     "arch": arch},
                    {}, {}, {})
    else:
        builder = build_template_default.get_builder(pure_c=False)
        items = []
        for item in builder.items:
            if item.options["icu:shared"] == True:
                items.append(item)
        builder.items = item

    builder.run()
