def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def find_fib(number):
    if number < 0:
        print("{} não faz parte da Sequência de Fibonacci".format(number))
        return False
    for i in range(number+2):
        if fib(i) == number:
            print("{} faz parte da Sequência de Fibonacci".format(number))
            return True
    print("{} não faz parte da Sequência de Fibonacci".format(number))
    return False

if __name__ == "__main__":
    number = int(input("Digite um número para saber se ele faz parte da Sequência de Fibonacci: "))
    find_fib(number)
    