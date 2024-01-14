#Let f be the function on natural numbers defined recursively as follows: f(0) = 0, f(n) = 2 * f(n/2) +1 if n > 0 and n is even, f(n) = 0 if n > 0 and n is odd. Write a Python function display_f(n), which given an integer n >= 0, prints out the value of f(0), f(1), ..., f(n).

def display_f(n):
    if n == 0:
        print(f'f({n}) = 0')
        return 0
    elif n % 2 == 0:
        previous_value = display_f(n // 2)
        result = 2 * previous_value + 1
        print(f'f({n}) = {result}')
        return result
    else:
        print(f'f({n}) = 0')
        return 0

display_f(100)
