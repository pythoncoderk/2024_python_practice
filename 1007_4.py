# 間違い探し

msg = "hello"

def say_hello():
    global msg
    msg += " "
    msg += "paiza"
    print(msg)

say_hello()
