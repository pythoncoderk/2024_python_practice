a = 999
l = []
def out(val):
    global a
    global l
    a = val
    l = l + ["python"]

out(111)
print(a)

print(l)