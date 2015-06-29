#!/usr/bin/python

import sys
from time import time
import subprocess
import re

def gen_program(n):
    field = lambda i: 'F%d { fldF%d :: ()}' % (i,i)
    s = 'module Mod(F(..)) where\n'
    s += \
         'data F\n' + \
         '  = ' + \
         '\n  | '.join(field(i) for i in range(n)) + '\n' + \
         '  deriving (Read)'
    return s

if False:
    with open('Mod.hs', 'w') as f:
        f.write(gen_program(int(sys.argv[1])))
else:
    for i in range(2, 13):
        n = int(2**i)
        with open('Mod.hs', 'w') as f:
            f.write(gen_program(n))

        for i in range(4):
            start = time()
            subprocess.check_call(['ghc', '-O', '-fforce-recomp', 'Mod.hs', '+RTS', '-sstderr.log'],
                                  stdout=sys.stderr)
            end = time()
            try:
                err = open('stderr.log').read()
                #print err
                alloc = int(re.search('([0-9,]+) bytes allocated in the heap', err).group(1).replace(',', ''))
                copied = int(re.search('([0-9,]+) bytes copied during GC', err).group(1).replace(',', ''))

                print n, end-start, alloc, copied
                sys.stdout.flush()
            except:
                pass

        print
