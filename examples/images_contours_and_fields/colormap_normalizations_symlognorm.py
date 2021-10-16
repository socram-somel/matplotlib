"""
==================================
Colormap Normalizations Symlognorm
==================================

Demonstration of using norm to map colormaps onto data in non-linear ways.

.. redirect-from:: /gallery/userdemo/colormap_normalization_symlognorm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

"""
SymLogNorm: two humps, one negative and one positive, The positive
with 5-times the amplitude. Linearly, you cannot see detail in the
negative hump.  Here we logarithmically scale the positive and
negative data separately.

Note that colorbar labels do not come out looking very good.
"""

N = 100
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = 5 * Z1 - Z2

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolormesh(X, Y, Z,
                       norm=colors.SymLogNorm(linthresh=0.5, linscale=1,
                                              vmin=-5, vmax=5, base=10),
                       cmap='RdBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='both')

pcm = ax[1].pcolormesh(X, Y, Z, cmap='RdBu_r', vmin=-5, vmax=5,
                       shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='both')

plt.show()
