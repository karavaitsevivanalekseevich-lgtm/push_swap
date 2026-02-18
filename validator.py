import sys
def validator(data):
    numbers = []
    for x in data:
        # Проверка что это число
        try:
            num = int(x)
        except ValueError:
            print("Error", file=sys.stderr)
            sys.exit(1)
        # Проверка границ int
        if not(-2147483648 <= num <= 2147483647):
            print("Error", file=sys.stderr)
            sys.exit(1)
        
        numbers.append(num)
    
    # Проверка дубликатов
    if len(numbers) != len(set(numbers)):
        print("Error", file=sys.stderr)
        sys.exit(1)
    return numbers


