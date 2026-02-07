import argparse


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


stack_a = Stack()
stack_b = Stack()

    
def sa(print_op=True): #Меняет местами первый и второй элемент a стека
    if len(stack_a.stack) in (0, 1):
        return
    first = stack_a.pop()
    second = stack_a.pop()
    stack_a.push(first)
    stack_a.push(second)
    if print_op:
        print("sa")
  
def sb(print_op=True): #Меняет местами первый и второй элемент b стека
    if len(stack_b.stack) in (0, 1):
        return
    first = stack_b.pop()
    second = stack_b.pop()
    stack_b.push(first)
    stack_b.push(second)
    if print_op:
        print("sb")

def ss(): #Меняет местами первый и второй элемент обоих стеков
    sa(print_op=False), sb(print_op=False)
    print("ss")

def pa(print_op=True): #Переложить с b на a
    if stack_b.is_empty():
        return
    else:
        stack_a.push(stack_b.pop())
        if print_op:
            print("pa")

def pb(print_op=True): #Переложить с a на b
    if stack_a.is_empty():
        return
    else:
        stack_b.push(stack_a.pop())
        if print_op:
            print("pb")

def ra(print_op=True): #Каждый элемент stack_a на один индекс меньше
    if len(stack_a.stack) > 1:
        tmp = stack_a.pop()
        tmp_arr = []
        while not stack_a.is_empty():
            tmp_arr.append(stack_a.pop())
            
        stack_a.push(tmp)
        for x in reversed(tmp_arr):
            stack_a.push(x)
        if print_op:    
            print("ra")    
      
            
def rb(print_op=True): #Каждый элемент stack_b на один индекс меньше
    if len(stack_b.stack) > 1:
        tmp = stack_b.pop()
        tmp_arr = []
        while not stack_b.is_empty():
            tmp_arr.append(stack_b.pop())
            
        stack_b.push(tmp)
        for x in reversed(tmp_arr):
            stack_b.push(x)
        if print_op:    
            print("rb")    
            
        
def rr(): #Каждый элемент stack_a и stack_b на один индекс меньше
    ra(print_op=False), rb(print_op=False)
    print("rr")    
                    


def rra(print_op=True): #Каждый элемент stack_a на один индекс больше
    if len(stack_a.stack) > 1:
        tmp_arr = []
        while not stack_a.is_empty():
            tmp_arr.append(stack_a.pop())
        
        tmp = tmp_arr[-1]  
        for x in reversed(tmp_arr[:-1]):  
            stack_a.push(x)
        stack_a.push(tmp)  
        if print_op:    
            print("rra")
            

def rrb(print_op=True): #Каждый элемент stack_b на один индекс больше
    if len(stack_b.stack) > 1:
        tmp_arr = []
        while not stack_b.is_empty():
            tmp_arr.append(stack_b.pop())
        
        tmp = tmp_arr[-1]
        for x in reversed(tmp_arr[:-1]):
            stack_b.push(x)
        stack_b.push(tmp)
        if print_op:    
            print("rrb")
        
         
def rrr(): #Каждый элемент stack_a и stack_b на один индекс больше
    rra(print_op=False), rrb(print_op=False)
    print("rrr")

    
parser = argparse.ArgumentParser()
parser.add_argument("numbers", nargs="*")
args = parser.parse_args()

array_to_stack = args.numbers


def validator(data):
    numbers = []
    for x in data:
        # Проверка что это число
        try:
            num = int(x)
        except ValueError:
            raise ValueError("Invalid Format")
        
        # Проверка границ int
        if not(-2147483648 <= num <= 2147483647):
            raise ValueError("Invalid Format")
        
        numbers.append(num)
    
    # Проверка дубликатов — после цикла
    if len(numbers) != len(set(numbers)):
        raise ValueError("Invalid Format")
    
    return numbers

stack_a.stack = validator(array_to_stack)


if stack_a.stack == sorted(stack_a.stack):
    exit()
    
def sort_three_and_less(nums:Stack):
    if not nums.is_empty():
        if len(nums.stack) == 1:
            return
        elif len(nums.stack) == 2:
            if nums.stack[0] < nums.stack[1]:
                return
            else:
                sa()
        elif len(nums.stack) == 3:        
            bot, mid, top = nums.stack[0], nums.stack[1], nums.stack[2]
            if bot < mid < top:  
                return
            elif bot < top < mid:  
                sa()
            elif mid < bot < top:  
                sa()
                ra()
            elif mid < top < bot:  
                rra()
            elif top < bot < mid:  
                ra()
            elif top < mid < bot:  
                sa()
                rra()
        
    
def check_sort(sorted_stack) -> bool:
    return sorted_stack.stack == sorted(sorted_stack.stack)
    

#First move будет перекидывать то что меньше медианы на стек б, больше отавит на стеке а
#Быстрая сортировка для 500 чисел, но вставкой для 100


def big_sort(stack): #Смотрит длину и взависимости от неё выбирает алгоритм
    if len(stack.stack) <= 3:
        sort_three_and_less(stack)
    elif len(stack.stack) <= 5:
        sort_five_and_four(stack)
    else:
        pass
    return stack.stack, check_sort(stack)
    
    
def sort_five_and_four(stack_to_sort: Stack):
    if len(stack_to_sort.stack) == 4:
        minium = min(stack_to_sort.stack)
        index = stack_to_sort.stack.index(minium)
        if index < len(stack_to_sort.stack) // 2: #Проверяем куда ближе индекс миниума к верху или низу
            while stack_to_sort.peek() != minium: #Перекидываем миниум в сторону верха
                rra()
        else:        
            while stack_to_sort.peek() != minium: #В сторону низа, где он становиться последним и идёт вверх
                ra()
        pb()
        sort_three_and_less(stack_to_sort)
        pa()
        ra() #Перекидываем на стек а, и вниз
    elif len(stack_to_sort.stack) == 5:
        minium = min(stack_to_sort.stack)
        index = stack_to_sort.stack.index(minium)
        if index < len(stack_to_sort.stack) // 2:
            while stack_to_sort.peek() != minium:
                rra()
        else:        
            while stack_to_sort.peek() != minium:
                ra()
        pb()
        minium = min(stack_to_sort.stack)
        index = stack_to_sort.stack.index(minium)
        if index < len(stack_to_sort.stack) // 2:
            while stack_to_sort.peek() != minium:
                rra()
        else:        
            while stack_to_sort.peek() != minium:
                ra()
        pb()
        sort_three_and_less(stack_to_sort)
        pa()
        ra() #Перекидываем на стек а, и вниз
        pa()
        ra() #Перекидываем на стек а, и вниз
        
print(big_sort(stack_a))        