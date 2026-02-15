from stack import Stack
from small_sort import quick_sort

def big_sort(nums: list):
    
    stack_a = Stack("a")
    stack_b = Stack("b")
    sorted_stack = quick_sort(nums)

    index = {}

    for x in sorted_stack:
        index[x] = sorted_stack.index(x)
    
    stack_a.stack = [index[x] for x in nums]
    
    n = 15 if len(stack_a.stack) <= 100 else 30
    counter = 0 #Это первая часть, она перекидывает элементы из а в б таким образом, что они становятся бабочкой
    while not stack_a.is_empty():
        if stack_a.peek() <= counter:
            stack_a.push_to(stack_b)
            stack_b.rotate()
            counter += 1
        elif stack_a.peek() <= counter + n: # Этот элиф как бы показывает что сейчас у нас самое большое из допустимых,
            #Просто запушим
            stack_a.push_to(stack_b)
            counter += 1
        else:
            stack_a.rotate()    
            
    #После 1 части стек б готов к тому чтобы мы его перекинули
    while not stack_b.is_empty():
        minimum= min(stack_b.stack)
        minimum_index = stack_b.stack.index(minimum)
        if len(stack_b.stack) // 2 > minimum_index:
            while stack_b.peek() != minimum:
                stack_b.reverse_rotate()
        else:
            while stack_b.peek() != minimum:
                stack_b.rotate()
        stack_b.push_to(stack_a)  
    print(stack_a.stack)      