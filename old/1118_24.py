def fizzbuzz(n):
    for i in range(1, n):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        print(result or i)



fizzbuzz(100)