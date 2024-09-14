first = int(input("enter first number: "))
second = int(input("enter second number: "))
op = input("enter operator(+,-,*,/,%): ")
if op=='+':
    sum = first+second
    print(sum)
elif op =='-':
    sub = first-second
    print(sub)
elif op=='*':
    mul = first*second
    print(mul)
elif op=='/':
    div = first/second
    print(div)
elif op=='%':
    rem = first%second
    print(rem)
else:
    print("wrong operator entered!")
