import turtle

fib_prev=1
fib_next=1

n=input()
n=int(n)

if n <=2:
    fib_n = 1
else:
    i = 3
    while i <=n:
        r=int(fib_next)
        a=90
        turtle.circle(r,a)
        i+=1
        fib_next, fib_prev = fib_prev + fib_next, fib_next
    fib_n = fib_next
print(fib_n)
