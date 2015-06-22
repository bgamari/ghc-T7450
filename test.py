#!/usr/bin/python

import sys
from time import time
import subprocess

def gen_program(n):
    field = lambda i: 'F%d { fldF%d :: ()}' % (i,i)
    s = 'module Mod(F(..)) where\n'
    s += \
         'data F\n' + \
         '  = ' + \
         '\n  | '.join(field(i) for i in range(n-1)) + '\n' + \
         '  deriving (Read)'
    return s

for n in [4000]:
    with open('Mod.hs', 'w') as f:
        f.write(gen_program(n))

    for i in range(10):
        start = time()
        subprocess.check_call(['/opt/exp/ghc/ghc/inplace/bin/ghc-stage2', '-O', '-fforce-recomp', 'Mod.hs'],
                              stdout=sys.stderr)
        end = time()
        print n, end-start
        sys.stdout.flush()

    print
