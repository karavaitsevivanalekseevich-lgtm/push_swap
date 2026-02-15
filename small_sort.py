from stack import Stack


def sort_three_and_less(stack_a: Stack):
        if not stack_a.is_empty():
            if len(stack_a.stack) == 1:
                return
            elif len(stack_a.stack) == 2:
                if stack_a.stack[0] > stack_a.stack[1]:
                    return
                else:
                    stack_a.swap()
            elif len(stack_a.stack) == 3:        
                bot, mid, top = stack_a.stack[0], stack_a.stack[1], stack_a.stack[2] #Вводим bot mid top для понятности
                if bot > mid > top:                #Т.к число перестановок 3 = 6, не стал ничего выдумывать и захардкодил
                    return
                elif bot > top > mid:  
                    stack_a.swap()
                elif bot < top < mid:
                    stack_a.reverse_rotate()
                elif mid > bot > top:  
                    stack_a.swap()
                    stack_a.rotate()
                elif top > bot > mid:  
                    stack_a.rotate()
                elif bot < mid < top:  
                    stack_a.swap()
                    stack_a.reverse_rotate()
                    
                    
def sort_five_and_four(stack_a: Stack, stack_b:Stack):
    if len(stack_a.stack) == 4:
        minium = min(stack_a.stack)
        index = stack_a.stack.index(minium)
        if index < len(stack_a.stack) // 2: #Проверяем куда ближе индекс миниума к верху или низу
            while stack_a.peek() != minium: #Перекидываем миниум в сторону верха
                stack_a.reverse_rotate()
        else:        
            while stack_a.peek() != minium: #В сторону низа, где он становиться последним и идёт вверх
                stack_a.rotate()
        stack_a.push_to(stack_b)
        sort_three_and_less(stack_a)
        stack_b.push_to(stack_a) #Перекидываем на а
    elif len(stack_a.stack) == 5:
        minium = min(stack_a.stack)
        index = stack_a.stack.index(minium)
        if index < len(stack_a.stack) // 2:
            while stack_a.peek() != minium:
                stack_a.reverse_rotate()
        else:        
            while stack_a.peek() != minium:
                stack_a.rotate()
        stack_a.push_to(stack_b)
        minium = min(stack_a.stack)
        index = stack_a.stack.index(minium)
        if index < len(stack_a.stack) // 2:
            while stack_a.peek() != minium:
                stack_a.reverse_rotate()
        else:        
            while stack_a.peek() != minium:
                stack_a.rotate()
        stack_a.push_to(stack_b)
        sort_three_and_less(stack_a)
        stack_b.push_to(stack_a)
        stack_b.push_to(stack_a) #Перекидываем на стек а

        
        
def small_sort(stack_a: Stack, stack_b: Stack):
    if len(stack_a.stack) <= 5:
        if len(stack_a.stack) <= 3:
            sort_three_and_less(stack_a)
        else:
            sort_five_and_four(stack_a, stack_b)
        
        
def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
