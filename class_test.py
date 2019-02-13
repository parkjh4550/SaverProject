from Memory import Memory


class DNC :
    def __init__(self):
        self.memory = Memory()

    def print_memory(self):
        return self.memory.number



if __name__ == '__main__':
    ncomputer = DNC()
    print('before initialize memory')
    print(ncomputer.print_memory(), '\n')

    ncomputer.memory.init_memory()
    print(ncomputer.print_memory())