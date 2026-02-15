class Stack:
    #Базовые операции
    def __init__(self, name):
        self.name = name
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
    
    
    def swap(self):
        if len(self.stack) in (0, 1):
            return
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        print("s" + self.name)
        
        
    def rotate(self):
        if len(self.stack) > 1:
            self.stack.insert(0, self.stack.pop())
            print("r" + self.name)    
             
                
    def reverse_rotate(self):
        if len(self.stack) > 1:
            self.stack.append(self.stack.pop(0))
            print("rr" + self.name)    
            
            
    def push_to(self, stack_to_push):
        if self.is_empty():
            return
        else:
            stack_to_push.push(self.pop())
            print("p" + stack_to_push.name)   
            

def rotate_both(stack_a, stack_b):
    if len(stack_a.stack) > 1 and len(stack_b.stack) > 1:
        stack_a.stack.insert(0, stack_a.stack.pop())
        stack_b.stack.insert(0, stack_b.stack.pop())
        print("rr")
        
     
def reverse_rotate_both(stack_a, stack_b):
    if len(stack_a.stack) > 1 and len(stack_b.stack) > 1:
        stack_a.stack.append(stack_a.stack.pop(0))
        stack_b.stack.append(stack_b.stack.pop(0))
        print("rrr")       


def swap_both(stack_a, stack_b):
    if len(stack_a.stack) > 1:
        stack_a.stack[-1], stack_a.stack[-2] = stack_a.stack[-2], stack_a.stack[-1]
    if len(stack_b.stack) > 1:
        stack_b.stack[-1], stack_b.stack[-2] = stack_b.stack[-2], stack_b.stack[-1]
    print("ss")
    