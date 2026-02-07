###Сюда нужно перенести реализация стека

class Stack:
    #Базовые операции
    def __init__(self):
        self.stack = []
    
    def push(self, node: int):
        self.stack.append(node)
    
    def pop(self):
        if not self.stack:
            raise IndexError("Your stack is empty")
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            raise IndexError("Your stack is empty")
        return self.stack[-1]
    
    def is_empty(self):
        return not self.stack

    #По хорошему лучше реализовать все операции (swap, push, rotate) как методы класса Stack.
    #Сейчас у тебя эти операции определены отдельно от стека и используют глобальные переменные

    
    def swap(self):#TODO
        pass

    def rotate(self):#TODO
        pass

    def reverse_rotate(self):
        pass

    def pop(self):#TODO
        pass
        #возвращает первый элемент стека
    
    def push(self, x):#TODO
        pass
        #кладет принимает элемент x в стек
