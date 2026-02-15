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
    
    # Проверка дубликатов
    if len(numbers) != len(set(numbers)):
        raise ValueError("Invalid Format")
    
    return numbers


