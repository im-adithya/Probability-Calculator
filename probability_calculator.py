import copy
import random

class Hat:
    def __init__ (self,**kwargs):
        self.contents = list()
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        self.length = len(self.contents)

    def draw(self,b):
        res = []
        if b>len(self.contents):
            res = self.contents
            self.contents = []
        else:
            for i in range(b):
                x = random.choice(self.contents)
                res.append(self.contents.pop(self.contents.index(x)))
        return res
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0
    for i in range(num_experiments):
        shat = copy.deepcopy(hat)
        arr = []
        item = dict()
        arr += shat.draw(num_balls_drawn)
        for i in arr:
            item[i] = item.get(i,0)+1
        if (all(item.get(k,0)-v>=0 for (k,v) in expected_balls.items())):
            prob+=1

    return prob/num_experiments