
def nine_times(x):
    def thrice(y):
        return y * 3
    return thrice(x) * 3


print(nine_times(2))
