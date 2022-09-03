import numpy as np

class Counter:
    def __init__(self):
        self.all_lb= []
        self.no_improve = 0

    def get_no_improve(self,lb):
        self.all_lb.append(lb)

        max_lb = np.max(self.all_lb)
        if max_lb > lb:
            self.no_improve = self.no_improve + 1
        else:
            self.no_improve = 0

        return self.no_improve




