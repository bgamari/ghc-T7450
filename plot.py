from matplotlib import pyplot as pl
import numpy as np
import scipy.optimize

a = np.genfromtxt('timing.log')
def model(x, m, a):
    return m * x**a
p,pcov = scipy.optimize.curve_fit(model, a[:,0], a[:,1])
print p
xs = np.linspace(min(a[:,0]), max(a[:,0]))
pl.plot(xs, model(xs, *p))
pl.plot(a[:,0], a[:,1], '+')
pl.yscale('log')
pl.xscale('log')
pl.xlabel('number of constructors')
pl.ylabel('runtime (seconds)')
pl.show()
