# -*- coding: utf-8 -*-
# author: itimor

import platform

if platform.node() == "jjyy":
    print("prod env")
    from aha.settings.base import *
    from aha.settings.prod import *
else:
    print("dev env")
    from aha.settings.base import *
    from aha.settings.dev import *
