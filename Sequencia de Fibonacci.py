print("#Sequencia de Fibonacci\n")

fib=list(range(200))
fib[0]=0
fib[1]=1

for i in range(2,200):
    fib[i]=fib[i-1]+fib[i-2]

a=int(input('Escolha um numero da sequencia de Fibonacci: '))
print(f'Fib({a})'
      f' = {fib[a]}')
