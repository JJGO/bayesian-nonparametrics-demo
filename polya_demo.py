#!/usr/bin/env python3

## Usage
# python polya_demo.py <a1> [<a2> ...]
# Enter <number> to draw <number> samples

import sys

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

from samplers import PolyaUrn

fig, (a0, a1) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[9, 1]}, figsize=(12,8))
fig.subplots_adjust(hspace=.5)

n=1000 #Number of frames

balls = [float(i) for i in sys.argv[1:]]
pol = PolyaUrn(*balls)

b = None
lines = None
its = 1
draws = 0


a0.set_xlabel('Colors', fontsize=16)
a0.set_ylabel('#Balls', fontsize=16)
a0.spines['right'].set_visible(False)
a0.spines['top'].set_visible(False)

a1.get_yaxis().set_visible(False)
a1.spines['right'].set_visible(False)
a1.spines['top'].set_visible(False)
a1.spines['left'].set_visible(False)
a1.set_xlim(0,1)


def animate(i):
    global pol, b, lines, its, draws

    if its == 0:
        s = input()
        if s == '':
            s = '1'
        its = int(s)

    its -= 1
    props = pol.proportions

    plt.gca().set_color_cycle(None)

    if b is not None:
        b.remove()
    if lines is not None:
        lines.remove()
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    b = a0.bar(np.arange(len(pol.balls)), pol.balls, color=colors)
    a0.set_xticks([], [])
    M = 2**np.ceil(np.log2(np.max(pol.balls)))
    a0.set_ylim(0,M)
    a1.set_title(r'Polya({})  #samples: {}'.format(", ".join(map(str,pol.balls)), draws), fontsize=18)
    left = 0
    for p in props:
        a1.barh(0, p, left=left)
        left += p

    t, u = next(pol)
    draws += 1
    lines = a1.axvline(u, color='k')

anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                             interval=10)

plt.show()