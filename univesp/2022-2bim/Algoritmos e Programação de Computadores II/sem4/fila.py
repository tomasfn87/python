class Fila:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        if type(item) in [list, tuple]:
            for i in item:
                self.data.append(i)
        else:
            self.data.append(item)

    def empty(self):
        return not len(self.data)

    def top(self):
        if not self.empty():
            return self.data[0]
        else:
            print('A fila está vazia.')
        
    def pop(self):
        return self.data.pop(0)

    def empty_me(self):
        content = []
        while not self.empty():
            content.append(self.pop())
        return content

    def size(self):
        return len(self.data)