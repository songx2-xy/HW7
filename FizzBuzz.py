def FizzBuzz(n):
    if n%5==0 and n%3==0:
        return "FizzBuzz"
    elif n%5==0:
        return "Buzz"
    elif n%3==0:
        return "Fizz"
    else:
        return n
for i in range(1,101):
    print(FizzBuzz(i))
