import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import sys

fig=plt.figure(figsize=(20,3))

alpha  = float(sys.argv[1])
# alpha = 100

n=500 #Number of frames
remainder = 1
uniform = -1

lines = None

draws = 0
rhos = 0
its = 1

def init():
    plt.xlim(0,1)
    plt.gca().get_yaxis().set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.title(r'$\rho \sim $GEM($\alpha=${})'.format(alpha), fontsize=20)

def animate(i):
    global remainder, uniform, lines, draws, rhos, its

    if uniform > 1 - remainder:
        V = np.random.beta(1, alpha)
        rho = V*remainder
        plt.barh(0, rho, left=1-remainder)
        remainder *= 1-V
        rhos += 1

    else:
        its -= 1
        if its == 0:
            s = input()
            if s == '':
                s = '1'
            its = int(s)
        if lines is not None:
            lines.remove()
        uniform = np.random.random()
        lines = plt.axvline(uniform, color='k')
        draws += 1

    plt.title(r'$\rho \sim $GEM($\alpha=${})        #$\rho$: {}       #samples: {}'.format(alpha, rhos, draws), fontsize=20)

anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                             interval=100, init_func=init)

plt.show()