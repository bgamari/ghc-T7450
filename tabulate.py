#!/usr/bin/python
# -- * encoding: utf-8 * --

import numpy as np
import sys

pre = np.genfromtxt(sys.argv[1], dtype=None, names='n,time,alloc,gc-copies')
post = np.genfromtxt(sys.argv[2], dtype=None, names='n,time,alloc,gc-copies')

ns = np.unique(np.hstack([pre['n'], post['n']]))
ns = [16, 64, 128, 256, 512, 1024, 2048, 4096]
write = sys.stdout.write

write('||= Number of constructors =||||||= allocated (MBytes) =||||||= time(s) =||=\n')
write('||= n =||= Pre-D1012 =||= Post-D1012 =||= Delta (%) =||= Post-D1012 =||= Post-D1012 =||= Delta (%) =||\n')

def stats(values):
    return '%1.2f ± %1.2f' % (values.mean(), values.std())

for n in ns:
    write('|| %d' % n)
    preA = pre[pre['n'] == n]['time']
    postA = post[post['n'] == n]['time']
    write('|| %s ' % stats(preA))
    write('|| %s ' % stats(postA))
    write('|| %2.0f%%' % ((postA.mean() - preA.mean()) / preA.mean() * 100))

    preA = pre[pre['n'] == n]['alloc'] / 1e6
    postA = post[post['n'] == n]['alloc'] / 1e6
    write('|| %s ' % stats(preA))
    write('|| %s ' % stats(postA))
    write('|| %2.0f%%' % ((postA.mean() - preA.mean()) / preA.mean() * 100))
    write('||\n')
