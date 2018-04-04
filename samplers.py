import numpy as np


class LazyGEM():

    def __init__(self, alpha):
        self.alpha = alpha
        self.rhos = []
        self.remainder = 1

    def __iter__(self):
        return self

    def __next__(self):
        u = np.random.uniform(0,1)
        acc = 0
        z = -1
        while acc < u:
            z += 1

            if u > 1 - self.remainder:
                V = np.random.beta(1, self.alpha)
                rho = V*self.remainder
                self.rhos.append(rho)
                self.remainder *= 1-V

            acc += self.rhos[z]

        return z


class PolyaUrn():

    def __init__(self, *balls):
        self.balls = list(balls)

    def __iter__(self):
        return self

    def __next__(self):
        u = np.random.uniform(0,1)
        acc = 0
        for color, p in enumerate(self.proportions):
            acc += p
            if u < acc:
                break
        self.balls[color] += 1
        return color, u

    @property
    def proportions(self):
        p = self.balls[:]
        p /= np.sum(p)
        return p

class CRP():

    def __init__(self, alpha):
        self.alpha = alpha
        self.tables = []

    def __iter__(self):
        return self

    def __next__(self):
        u = np.random.uniform(0,1)
        acc = 0
        for table, p in enumerate(self.proportions):
            acc += p
            if u < acc:
                break

        if table == len(self.proportions)-1:
            self.tables.append(1)
        else:
            self.tables[table] += 1
        return table, u

    @property
    def proportions(self):
        p = self.tables+[self.alpha]
        p /= np.sum(p)
        return p


