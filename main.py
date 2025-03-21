def fizzbuzz(n):
    if n%3 and n%5:
        return "FizzBuzz"
    elif n%3:
        return "Fizz"
    elif n%5:
        return "Buzz"
    else:
        return str(n)


def main():
    n= int(input("Enter a number: "))
    print(fizzbuzz(n))

if __name__ == "__main__":
   main()