def pertence_a_fibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    
    return False

num = 8

if pertence_a_fibonacci(num):

    print(f"O número {num} pertence a sequência de Fibonacci.")

else:

    print(f"O número {num} não pertence a sequência de Fibonacci.")