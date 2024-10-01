# 以下のコードを修正 
def give_an_honorific(names):
    for i in range(len(names)):
        names[i] += "san"
    return names


names = ["kirishima", "midorikawa"]
print(give_an_honorific(names))
print(names)
