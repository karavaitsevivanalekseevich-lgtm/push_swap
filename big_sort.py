from stack import Stack

#Здесь реализовать основной алгоритм

#Скелет функции которая делает основную сортировку
def big_sort_algorithm(numbers: list):

    #создаем два стека внутри функции
    stack_a = Stack()
    stack_b = Stack()

    #пушим все элементы из массива в стек
    for x in numbers:
        stack_a.push(x) #пользуемся реализованными методами класса Stack

    sorted_array = []
    actions = []
    #реализуем логику сортировки и трекаем действия...
    return actions, sorted_array