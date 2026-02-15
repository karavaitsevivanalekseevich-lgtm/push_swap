import argparse
from stack import Stack
from small_sort import small_sort, quick_sort
from validator import validator
from big_sort import big_sort


parser = argparse.ArgumentParser()
parser.add_argument("numbers", nargs="*")
args = parser.parse_args()

array = args.numbers 

unsorted = validator(array) #Просто получение и валидация данных

if all(unsorted[i] <= unsorted[i+1] for i in range(len(unsorted) - 1)): #Проверка на отсортированность
    exit()

if len(unsorted) <= 5:          #Ветвление, которое определит какой алгоритм сортировки брать
    stack_a = Stack("a")
    stack_b = Stack("b")
    stack_a.stack = list(reversed(unsorted))
    small_sort(stack_a, stack_b)
    exit()

else:
    big_sort(unsorted)
    