N = int(input())

def factorial(num, result):
    if num == 1:
        return result
    
    return(factorial(num - 1, result * num))

print(factorial(N, 1))