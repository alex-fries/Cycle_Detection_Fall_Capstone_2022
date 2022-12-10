"""
pulled from https://github.com/janvdl/python_tarjan/blob/master/tarjan.py
"""
from copy import deepcopy
class TarjinAlgo(object):

    def __init__(self, g):
        #self.G_ = [[5, 9], [7, 9], [6, 9], [5], [5, 6, 7], [1], [3], [2], [1], [4]]
        self.G_ = g
        self.cycles = []

        self.point_stack = []
        self.marked = []
        self.marked_stack = []

        self.entry_tarjan(self.G_)
        #print(self.cycles)

    def tarjan(self, s, v):
        self.f = False
        self.point_stack.append(v)
        self.marked[v] = True
        self.marked_stack.append(v)
        for w in self.G[v]:
            if w<s:
                self.G[w] = 0
            elif w == s:
                self.cycles.append(list(deepcopy(self.point_stack)))
                self.f = True
            elif self.marked[w] == False:
                self.g = self.tarjan(s,w)
                self.f = self.f or self.g
                
        if self.f == True:
            while self.marked_stack[len(self.marked_stack) - 1] != v:
                u = self.marked_stack.pop()
                self.marked[u] = False
            self.marked_stack.pop()
            self.marked[v] = False
            
        self.point_stack.pop()
        return self.f
            
    def entry_tarjan(self, G_):
        self.G = deepcopy(self.G_)

        self.marked = [False for x in range(0, len(G_))]
        
        for i in range(len(self.G)):
            self.tarjan(i, i)
            while self.marked_stack:
                u = self.marked_stack.pop()
                self.marked[u] = False
        
        #return self.cycles

    def returnCycles(self):
        return self.cycles