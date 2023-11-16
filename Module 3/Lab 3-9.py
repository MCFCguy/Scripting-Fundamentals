for num in range(10, 100):
    if num % 5 == 0:
        if num == 95:
            break
        print(num)
    elif type(num) != int:
        continue
    else:
        pass
    
