def fibonachy(n):

    if n < 0:
        raise ValueError("n должно быть неотрицательным")

    fib1 = fib2 = 1

    fib = []
    if n==0 :
        fib.append(0)

    if n==1:
        fib.append(0)
        fib.append(fib1)

    if n==2:
        fib.append(0)
        fib.append(fib1)
        fib.append(fib2)

    if n>2:
        fib.append(0)
        fib.append(fib1)
        fib.append(fib2)
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            fib.append(fib2)

    return fib

def sort(a):

    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("такой оператор пока не поддерживается")