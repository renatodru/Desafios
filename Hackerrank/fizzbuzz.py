def fizzBuzz(n):    
    # Write your code here
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
    
if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)