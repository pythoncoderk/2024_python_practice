message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    global message
    print(message + " " + str(a))
    return x + y

num = sum(3, 2)
print(num)
print(message + " " + str(a))