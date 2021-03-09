class WelfordVar:
    def __init__(self):
        self.n = 0
        self.E = 0
        self.M = 0
    def update(self, x):
        self.M += self.n*(x-self.E)**2/(self.n+1)
        self.E = self.n*self.E/(self.n+1) + x/(self.n+1)
        self.n += 1
    def var(self, ddof=0):
        return self.M/(self.n-ddof)
    def mean(self):
        return self.E
    
if __name__ == '__main__':
    import numpy as np
    X = np.random.rand(10, 5)
    wv = WelfordVar()
    it = iter(X)
    while True:
        try:
            wv.update(next(it))
        except:
            break
    print(wv.var())
    print(np.var(X,axis=0))
