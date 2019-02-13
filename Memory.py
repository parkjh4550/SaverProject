import numpy as np

class Memory:
    def __init__(self, word_num= 60, word_size=30):
        self.number = 0

    def init_memory(self):
        self.number = 1
        print('initialize memory number')