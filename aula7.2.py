import random

def lancar_dados():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')

lancar_dados()
