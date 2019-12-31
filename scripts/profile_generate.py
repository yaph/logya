#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logya.generate import Generate

import cProfile, pstats, io
from pstats import SortKey


pr = cProfile.Profile()
pr.enable()

Generate(verbose=True)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
ps.print_stats()
print(s.getvalue())
